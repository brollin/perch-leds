import math
from pattern import Pattern
from util import lerp3

BLUE = (43, 174, 140)
ORANGE = (231, 50, 1)

class Bladerunner(Pattern):
    frame = 0
    def __init__(self, pixel_config) -> None:
        super().__init__(pixel_config)

    def progress(self):
        count = self.pixel_config.count
        self.frame = (self.frame + 1) % 200
        start = round(count * 0.3) + round(count * 0.2) * math.sin(self.frame * 2 * math.pi / 100)
        stop = round(count * 0.7) + round(count * 0.2) * math.cos(self.frame * 2 * math.pi / 200)

        for i in range(count):
            if i < start:
                self.pixel_config.pixels[i] = BLUE
            elif i < stop:
                self.pixel_config.pixels[i] = lerp3(i, start, stop, BLUE, ORANGE)
            else:
                self.pixel_config.pixels[i] = ORANGE
