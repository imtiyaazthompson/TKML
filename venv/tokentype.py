import enum


class TokenType(enum.Enum):

    LABEL = 0
    BUTTON = 1

    def __str__(self):
        return self.name
