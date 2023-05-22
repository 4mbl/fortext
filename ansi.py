from enum import Enum, IntEnum

ESC = '\033['
RESET = f'{ESC}0m'


class Fg(Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    DEFAULT = 39


class Bg(Enum):
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47
    DEFAULT = 49


class Style(IntEnum):
    DEFAULT = 0
    BOLD = 1
    ITALIC = 3
    UNDERLINE = 4
    BLINK_SLOW = 5
    BLINK_FAST = 6
    REVERSE = 7
    HIDE = 8
    STRIKETHROUGH = 9
