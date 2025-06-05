from enum import Enum

class Genre(str, Enum):
    history = "History"
    philosophy = "Philosophy"
    science = "Science"