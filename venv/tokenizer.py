from token import Token
from tokentype import TokenType
from exceptionlib import InvalidTokenException, TokenTextException
import re


def tokenize(line):
    print(line)
    # Match in groups for easy extrapolation of data
    pattern_type_name = "\[([a-z]+):(.+)\]"
    pattern_args = "\((width=\"(\d*)\"\s+height=\"(\d*)\"\s+bg=\"([a-z|0-9]*)\"\s+fg=\"([a-z|0-9]*)\")*\)"
    pattern_msg = ":\"(\s*.*)\""

    # Match token type, arguments and message
    # re.search searches anywhere in the string, not just the beginning
    match_type_name = re.search(pattern_type_name, line)
    match_args = re.search(pattern_args, line)
    match_msg = re.search(pattern_msg, line)

    # Generate token
    token_type, token_name = get_type_name(match_type_name)
    arguments = get_args(match_args)
    message = get_message(match_msg)

    print("\Valid token")
    return Token(token_type, token_name, arguments, message)


def get_type_name(match):
    if match is None:
        raise InvalidTokenException("Token incorrectly named")

    tok_type = match.groups()[0]
    name = match.groups()[1]

    ttype = None
    if tok_type == "label":
        ttype = TokenType.LABEL
    if tok_type == "button":
        ttype = TokenType.BUTTON

    return ttype, name


def get_args(match):
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


def get_message(match):
    if match is None:
        raise TokenTextException("Token text incorrectly formatted")

    return match.groups()[0]


def main():
    token = tokenize("[label](): Hello, World")
    print(token)


if __name__ == "__main__":
    main()
