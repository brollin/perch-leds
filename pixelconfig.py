import board
import neopixel

class PixelConfig:
    # frames per second. this is an upper bound since pattern computation time will only lower fps.
    # this can be overridden by patterns
    default_fps = 30

    # total number of LEDs
    count = 150

    def __init__(self) -> None:
        self.pixels = neopixel.NeoPixel(
            board.GP0,
            self.count,
            auto_write=False,
            brightness=0.3,
            pixel_order=neopixel.GRB
        )
