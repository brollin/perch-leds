import board
import neopixel
import time

from bladerunner import Bladerunner
from fire2012 import Fire2012
from fadeout import Fadeout


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

# flash blue for one second as indication of successful startup
for i in range(pixel_config.count):
    pixel_config.pixels[i] = (50, 125, 200)
pixel_config.pixels.show()
time.sleep(1)

patterns = [
    Bladerunner(pixel_config),
    Fadeout(pixel_config),
    Fire2012(pixel_config),
]
pattern_index = 0
pattern = patterns[pattern_index]
frames = 0

while True:
    # advance frames, pattern if necessary
    frames = (frames + 1) % (pattern.duration * pixel_config.fps)
    if frames == 0 or pattern.finished:
        pattern_index = (pattern_index + 1) % len(patterns)
        pattern = patterns[pattern_index]
        pattern.initialize()

    pattern.progress()
    pixel_config.pixels.show()
    time.sleep(1 / pixel_config.fps)
