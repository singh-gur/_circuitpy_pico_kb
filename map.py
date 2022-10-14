# Map for 3 row 4 column
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode


MEDIA = 1
KEY = 2

keymap = {
    (0): (KEY, [Keycode.ENTER]),
    (1): (KEY, [Keycode.SHIFT, Keycode.F14]),
    (2): (KEY, [Keycode.SHIFT, Keycode.F15]),
    (3): (KEY, [Keycode.SHIFT, Keycode.F16]),

    (4): (KEY, [Keycode.ALT, Keycode.F13]),
    (5): (KEY, [Keycode.ALT, Keycode.F14]),
    (6): (KEY, [Keycode.ALT, Keycode.F15]),
    (7): (KEY, [Keycode.ALT, Keycode.F16]),

    (8): (KEY, [Keycode.EIGHT]),
    (9): (KEY, [Keycode.NINE]),
    (10): (KEY, [Keycode.CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW]),
    (11): (KEY, [Keycode.CONTROL, Keycode.WINDOWS, Keycode.RIGHT_ARROW]),
}
