from _widget import Token
from widget_type import WidgetType
from exceptionlib import InvalidTokenException, TokenTextException
import re


def tokenize(line):
    """Generate Token objects from each line of parsed input"""

    # Match in groups for easy extrapolation of data
    pattern_type_name = "\[([a-z]+):(.+)\]"
    pattern_args_lb = "\((width=\"(\d*)\"\s+height=\"(\d*)\"\s+bg=\"([a-z|0-9]*)\"\s+fg=\"([a-z|0-9]*)\")*\)"
    pattern_args_entry = "\((fg=\"([a-z|0-9]*)\"\s+bg=\"([a-z|0-9]*)\"\s+width=\"(\d*)\")*\)"
    pattern_msg = ":\"(\s*.*)\""

    # Match token type, arguments and message
    # re.search searches anywhere in the string, not just the beginning
    match_type_name = re.search(pattern_type_name, line)
    token_type, token_name = get_type_name(match_type_name)
    if token_type == WidgetType.ENTRY:
        match_args = re.search(pattern_args_entry, line)
        arguments = get_args_entry(match_args)
    else:
        match_args = re.search(pattern_args_lb, line)
        arguments = get_args_lb(match_args)

    match_msg = re.search(pattern_msg, line)

    # Generate token
    message = get_message(match_msg)

    return Token(token_type, token_name, arguments, message)


def get_type_name(match):
    """Get the type and name of the widget specified in the parsed input string"""
    if match is None:
        raise InvalidTokenException("Token incorrectly named")

    tok_type = match.groups()[0]
    name = match.groups()[1]

    ttype = None
    if tok_type == "label":
        ttype = WidgetType.LABEL
    if tok_type == "button":
        ttype = WidgetType.BUTTON
    if tok_type == "entry":
        ttype = WidgetType.ENTRY

    return ttype, name


def get_args_lb(match):
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


def get_args_entry(match):
    """Get the widget arguments for a entry type widget"""
    fg = match.groups()[1] if match.groups()[1] is not None else ""
    bg = match.groups()[2] if match.groups()[2] is not None else ""
    width = match.groups()[3] if match.groups()[3] is not None else ""

    return {
        "fg": fg,
        "bg": bg,
        "width": width
    }


def get_message(match):
    """Get the text label of the widget"""
    if match is None:
        raise TokenTextException("Token text incorrectly formatted")

    return match.groups()[0]


def main():
    token = tokenize("[label](): Hello, World")
    print(token)


if __name__ == "__main__":
    main()
