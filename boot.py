from errno import EALREADY
from board import GP11
from digitalio import DigitalInOut, Direction, Pull
from storage import disable_usb_drive
from usb_cdc import disable

enable_pin = GP11
enable_switch = DigitalInOut(enable_pin)
enable_switch.direction = Direction.INPUT
enable_switch.pull = Pull.UP

if not enable_switch.value:
    disable_usb_drive()
    disable()


