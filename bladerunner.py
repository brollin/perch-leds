from pattern import Pattern
from util import lerp3, random_sin_cycler

BLACK = (0, 0, 0)
BLUE = (43, 174, 140)
ORANGE = (231, 50, 1)

class Bladerunner(Pattern):
    def initialize(self):
        super().initialize()

        self.faded_in_percent = 0
        self.start_cycler = random_sin_cycler(60, 200)
        self.stop_cycler = random_sin_cycler(60, 200)

    def progress(self):
        count = self.pixel_config.count
        start = round(count * 0.15) + round(count * 0.3) * next(self.start_cycler)
        stop = round(count * 0.85) + round(count * 0.3) * next(self.stop_cycler)

        for i in range(count):
            if i < start:
                self.pixel_config.pixels[i] = BLUE
            elif i < stop:
                self.pixel_config.pixels[i] = lerp3(i, start, stop, BLUE, ORANGE)
            else:
                self.pixel_config.pixels[i] = ORANGE

        # slowly fade in as the pattern is progressing over 100 frames
        if self.faded_in_percent < 100:
            self.faded_in_percent += 1
            for i, pixel in enumerate(self.pixel_config.pixels):
                    self.pixel_config.pixels[i] = lerp3(self.faded_in_percent, 0, 100, BLACK, pixel)
