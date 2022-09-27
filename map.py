# Map for 3 row 4 column
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


MEDIA = 1
KEY = 2

keymap = {
    (0): (KEY, [Keycode.ENTER]),
    (1): (KEY, [Keycode.F14]),
    (2): (KEY, [Keycode.F15]),
    (3): (KEY, [Keycode.F16]),

    (4): (KEY, [Keycode.FOUR]),
    (5): (KEY, [Keycode.FIVE]),
    (6): (KEY, [Keycode.SIX]),
    (7): (KEY, [Keycode.SEVEN]),

    (8): (KEY, [Keycode.EIGHT]),
    (9): (KEY, [Keycode.NINE]),
    (10): (KEY, [Keycode.A]),
    (11): (KEY, [Keycode.B]),
}