from codegen import gen_source
from tkmlparser import Parser
from tokenizer import Tokenizer
from exceptionlib import TokenException, BrokenFrameException
from widget_type import WidgetType


def main():
    # Parse tkml file
    p = Parser('test.tkml')
    t = Tokenizer()

    # Parse till EOF
    tokens = []
    packing = []
    in_frame = False
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
                elif next_token.get_type() == WidgetType.ENDFRAME:
                    in_frame = False

                # Append tokens within the current frame
                # Tokens for each frame need to be sorted according to precedence later
                tokens.append(next_token)
                if next_token.get_type() != WidgetType.ENDFRAME:
                    packing.append(next_token.get_name())  # Preserve user order for packing widgets

    # If still within a frame, raise exception
    if in_frame:
        raise BrokenFrameException("A frame was not closed correctly")

    # Sort Tokens
    # Ensure widgets are written to source according to type precedence
    tokens.sort(key=lambda token: token.get_type())
    # Source Code generation
    gen_source(tokens, packing)
    print("Template produced successfully!")


if __name__ == "__main__":
    main()
