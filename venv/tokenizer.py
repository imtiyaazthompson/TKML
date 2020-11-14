from _widget import Token
from widget_type import WidgetType
from exceptionlib import InvalidTokenException, TokenTextException, BrokenFrameException
import re


# Converted from static to Class to make use of static variable to count
# nesting of frames

class Tokenizer:
    static_endframe_counter = 0
    static_frame_stack = []

    def tokenize(self, line):
        """Generate Token objects from each line of parsed input"""

        # Match in groups for easy extrapolation of data
        pattern_type_name = "\[([a-z]+):(.+)\]"
        pattern_args_lb = "\((width=\"(\d*)\"\s+height=\"(\d*)\"\s+bg=\"([a-z|0-9]*)\"\s+fg=\"([a-z|0-9]*)\")*\)"
        pattern_args_entry = "\((fg=\"([a-z|0-9]*)\"\s+bg=\"([a-z|0-9]*)\"\s+width=\"(\d*)\")*\)"
        pattern_msg = ":\"(\s*.*)\""
        pattern_endframe = "(\s*\})"

        # Match token type, arguments and message
        # re.search searches anywhere in the string, not just the beginning
        if "}" not in line:
            match_type_name = re.search(pattern_type_name, line)
        else:
            match_type_name = re.search(pattern_endframe, line)
        token_type, token_name = self.get_type_name(match_type_name)

        if token_type == WidgetType.STARTFRAME:
            match = re.search("\s*\{", line)
            if match is None:
                raise BrokenFrameException("Opening frame delimiter is missing")
            else:
                self.static_frame_stack.insert(0, token_name)
                return Token(token_type, token_name, None, None)

        if token_type == WidgetType.ENDFRAME:
            return Token(token_type, token_name, None, None)

        if token_type == WidgetType.ENTRY:
            match_args = re.search(pattern_args_entry, line)
            arguments = self.get_args_entry(match_args)
        elif token_type == WidgetType.STARTFRAME or token_type == WidgetType.ENDFRAME:
            return Token(token_type, token_name, None, None)
        else:
            match_args = re.search(pattern_args_lb, line)
            arguments = self.get_args_lb(match_args)

        match_msg = re.search(pattern_msg, line)

        # Generate token
        message = self.get_message(match_msg)

        return Token(token_type, token_name, arguments, message)

    def get_type_name(self, match):
        """Get the type and name of the widget specified in the parsed input string"""
        if match is None:
            raise InvalidTokenException("Token incorrectly named")

        if len(match.groups()) != 1:
            tok_type = match.groups()[0]
            name = match.groups()[1]
        else:
            tok_type = (match.groups()[0]).strip()
            name = f"endframe_{(self.static_frame_stack.pop(0))}"
            self.static_endframe_counter += 1

        ttype = None
        if tok_type == "label":
            ttype = WidgetType.LABEL
        if tok_type == "button":
            ttype = WidgetType.BUTTON
        if tok_type == "entry":
            ttype = WidgetType.ENTRY
        if tok_type == "frame":
            ttype = WidgetType.STARTFRAME
        if tok_type == "}":
            ttype = WidgetType.ENDFRAME

        return ttype, name

    def get_args_lb(self, match):
        """Get the widget arguments for a button/label type widget"""
        width = match.groups()[1] if match.groups()[1] is not None else ""
        height = match.groups()[2] if match.groups()[2] is not None else ""
        bg = match.groups()[3] if match.groups()[3] is not None else ""
        fg = match.groups()[4] if match.groups()[4] is not None else ""

        return {
            "width": width,
            "height": height,
            "bg": bg,
            "fg": fg
        }

    def get_args_entry(self, match):
        """Get the widget arguments for a entry type widget"""
        fg = match.groups()[1] if match.groups()[1] is not None else ""
        bg = match.groups()[2] if match.groups()[2] is not None else ""
        width = match.groups()[3] if match.groups()[3] is not None else ""

        return {
            "fg": fg,
            "bg": bg,
            "width": width
        }

    def get_message(self, match):
        """Get the text label of the widget"""
        if match is None:
            raise TokenTextException("Token text incorrectly formatted")

        return match.groups()[0]
