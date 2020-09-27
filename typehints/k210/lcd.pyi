from typing import Any, Tuple, Union, Optional

BLACK: int = 0x0000
NAVY: int = 0x0F00
DARKGREEN: int = 0xE003
DARKCYAN: int = 0xEF03
MAROON: int = 0x0078
PURPLE: int = 0x0F78
OLIVE: int = 0xE07B
LIGHTGREY: int = 0x18C6
DARKGREY: int = 0xEF7B
BLUE: int = 0x1F00
GREEN: int = 0xE007
CYAN: int = 0xFF07
RED: int = 0x00F8
MAGENTA: int = 0x1FF8
YELLOW: int = 0xE0FF
WHITE: int = 0xFFFF
ORANGE: int = 0x20FD
GREENYELLOW: int = 0xE5AF
PINK: int = 0x1FF8

XY_RLUD: int = 0x00
YX_RLUD: int = 0x20
XY_LRUD: int = 0x40
YX_LRUD: int = 0x60
XY_RLDU: int = 0x80
YX_RLDU: int = 0xA0
XY_LRDU: int = 0xC0
YX_LRDU: int = 0xE0


def init(type: Optional[int] = 1, freq: int = 15000000, color: Union[Tuple, int] = BLACK) -> None:
    """
    Initialize the LCD screen to display.

    :param type: type of LCD 0: None 1: lcd shield (default).
    :param freq: frequency of lcd.
    :param color: LCD initialized color, 16 bits RGB565 color, e.g. 0xFFFF; or RGB888 tuple, e.g. (236, 36, 36), default lcd.BLACK.
    """


def deinit() -> None:
    """
    Unregister the LCD driver to release the I/O pins.

    """


def width() -> int:
    """
    Returns the width of the LCD (horizontal resolution).

    """


def height() -> int:
    """
    Returns the height of the LCD (vertical resolution).

    """


def type() -> int:
    """
    Returns the type of LCD (reserved for future use).

    :return: 0: None 1: lcd Shield.
    """


def freq(freq: Optional[int] = None) -> int:
    """
    Set or get frequency of LCD (SPI).

    :param freq: frequency of LCD (SPI).
    :return: frequency of LCD.
    """


def set_backlight(state: int) -> None:
    """
    Setting the backlight status of LCD, turning off the backlight will greatly reduce the energy consumption of the LCD expansion board.
    //TODO: Not implemented.

    :param state: backlight brightness, value [0,100].
    """


def get_backlight() -> int:
    """
    Return to backlight status.

    :return: Backlight brightness, value [0,100].
    """


def display(image: Any, roi: Optional[Tuple[int, int, int, int]] = None) -> None:
    """
    Display a image (GRAYSCALE or RGB565) on the LCD.

    roi is a key-value parameter that must be explicitly called by writing roi= in a function call.

    :param image: image (GRAYSCALE or RGB565).
    :param roi: a rectangular tuple (x, y, w, h) of a region of interest. If not specified, it is an image rectangle.
    """


def clear(color: Union[Tuple, int] = BLACK) -> None:
    """
    Empty the LCD screen to black or other color.

    :param color: LCD initialized color, 16 bits RGB565 color, e.g. 0xFFFF; or RGB888 tuple, e.g. (236, 36, 36).
    """


def direction(dir: int) -> None:
    """
    Set LCD direction and mirror.

    It has been discard after v0.3.1, use lcd.rotation and lcd.mirror instead.

    :param dir: nomally lcd.YX_LRUD or lcd.YX_RLDU, other values just exchange XY or LR or DU.
    """


def rotation(dir: Optional[int] = None) -> int:
    """
    Set LCD direction.

    :param dir: value [0,3], turn clockwise from 0 to 3.
    :return: Current direction, value [0,3].
    """


def mirror(invert: Optional[bool] = None) -> bool:
    """
    Set LCD mirror.

    :param invert: mirror display, True or False.
    :return: Current config, True or False.
    """


def draw_string(x: int, y: int, str: str, color: Optional[int] = None) -> None:
    """
    Display English.

    """
