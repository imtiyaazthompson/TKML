import enum


class WidgetType(enum.Enum):

    # Precedence of tokens
    STARTFRAME = -1
    LABEL = 0
    ENTRY = 1
    FIELD = 2
    BUTTON = 3
    ENDFRAME = 4

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
