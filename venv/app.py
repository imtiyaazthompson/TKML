from codegen import gen_source
from tkmlparser import Parser
from tokenizer import Tokenizer
from exceptionlib import TokenException, BrokenFrameException
from widget_type import WidgetType
import re


def main():
    # Parse tkml file
    p = Parser('test.tkml')
    t = Tokenizer()

    # Parse till EOF
    tokens = []
    packing = []
    in_frame = False
    frame_stack = []
    while True:
        next_line = p.get_next_line()
        if next_line == "":
            break
        else:
            next_token = t.tokenize(next_line)
            if next_token in tokens:
                raise TokenException("Duplicate token name encountered: " + next_token.get_name())
            else:
                # Checking if Framing is complete
                if next_token.get_type() == WidgetType.STARTFRAME:
                    in_frame = True
                    frame_stack.insert(0, next_token.get_name())

                    # Set parents of frames
                    next_token.parent = frame_stack[1] if len(frame_stack) >= 2 else None
                elif next_token.get_type() == WidgetType.ENDFRAME:
                    in_frame = False
                    parent = (re.search("_(.+)", next_token.get_name())).groups()[0]
                    # if the endframe does not belong to the proper start frame
                    if parent != frame_stack[0]:
                        raise BrokenFrameException("A Frame was not closed correctly")
                    frame_stack.pop(0)
                else:
                    # Set the parent of the current token that is not a frame
                    next_token.parent = frame_stack[0]

                # Append tokens within the current frame
                # Tokens for each frame need to be sorted according to precedence later
                tokens.append(next_token)
                if next_token.get_type() != WidgetType.ENDFRAME:
                    packing.append(next_token.get_name())  # Preserve user order for packing widgets

    # If still within a frame, raise exception
    # Or if a frame was not closed properly, thus it not being removed from the stack
    # Number start frames does not match the number of end frames
    if in_frame or frame_stack != []:
        raise BrokenFrameException("A frame was not closed correctly")

    # Sort Tokens
    # Ensure widgets are written to source according to type precedence
    tokens.sort(key=lambda token: token.get_type())
    # Source Code generation
    gen_source(tokens, packing)
    print("Template produced successfully!")


if __name__ == "__main__":
    main()
