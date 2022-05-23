from pattern import Pattern
from util import lerp3

blue = (43, 174, 140)
orange = (231, 50, 1)

class Bladerunner(Pattern):
    def __init__(self, pixel_config) -> None:
        super().__init__(pixel_config)

    def progress(self):
        count = self.pixel_config.count
        start = round(count * 0.1)
        stop = round(count * 0.9)

        for i in range(count):
            if i < start:
                self.pixel_config.pixels[i] = blue
            elif i < stop:
                self.pixel_config.pixels[i] = lerp3(i, start, stop, blue, orange)
            else:
                self.pixel_config.pixels[i] = orange
