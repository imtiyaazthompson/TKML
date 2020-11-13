class TokenException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidTokenException(Exception):
    def __init__(self, message):
        super().__init__(message)


class TokenTextException(Exception):
    def __init__(self, message):
        super().__init__(message)

