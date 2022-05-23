import board
import neopixel
import time

from fire2012 import Fire2012
from bladerunner import Bladerunner


class PixelConfig:
    fps = 30
    count = 120
    def __init__(self) -> None:
        self.pixels = neopixel.NeoPixel(
            board.GP0,
            self.count,
            auto_write=False,
            brightness=0.3,
            pixel_order=neopixel.GRB
        )

pixel_config = PixelConfig()
fire2012 = Fire2012(pixel_config)
bladerunner = Bladerunner(pixel_config)

# flash blue as indication of reset
for i in range(pixel_config.count):
    pixel_config.pixels[i] = (50, 125, 200)
pixel_config.pixels.show()
time.sleep(1)

while True:
    bladerunner.progress()
    # fire2012.progress()
    pixel_config.pixels.show()
    time.sleep(1 / pixel_config.fps)

