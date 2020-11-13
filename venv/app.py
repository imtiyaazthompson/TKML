from codegen import gen_source
from tkmlparser import Parser
from tokenizer import tokenize
from exceptionlib import TokenException


def main():
    # Parse tkml file
    p = Parser('test.tkml')

    # Parse till EOF
    tokens = []
    packing = []
    while True:
        next_line = p.get_next_line()
        if next_line == "":
            break
        else:
            next_token = tokenize(next_line)
            if next_token in tokens:
                raise TokenException("Duplicate token name encountered: " + next_token.get_name())
            else:
                tokens.append(next_token)
                packing.append(next_token.get_name()) # Preserve user order for packing widgets

    # Sort Tokens
    # Ensure widgets are written to source according to type precedence
    tokens.sort(key = lambda token: token.get_type())
    # Source Code generation
    gen_source(tokens,packing)
    print("Template produced successfully!")


if __name__ == "__main__":
    main()