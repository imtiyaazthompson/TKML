from codegen import gen_source
from tkmlparser import Parser
from tokenizer import tokenize
from exceptionlib import TokenException


def main():
    # Parse tkml file
    p = Parser('test.tkml')

    # Parse till EOF
    tokens = []
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

    # Source Code generation
    gen_source(tokens)


if __name__ == "__main__":
    main()