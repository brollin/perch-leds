from random import random
from pattern import Pattern

TEAL = (19, 241, 242)
BLUE = (59, 94, 166)
PURPLE = (115, 21, 114)
MAGENTA = (192, 0, 80)
RED = (255, 38, 54)
YELLOW = (255, 170, 26)
COLORS = [TEAL, BLUE, PURPLE, MAGENTA, RED, YELLOW]

class Tron(Pattern):
    duration = 6000
    fps = 60

    def initialize(self):
        super().initialize()

        self.color_index = 0
        self.length = 0
        self.direction = -1 if random() > 0.5 else 1

    def progress(self):
        count = self.pixel_config.count
        if self.direction == -1:
            self.pixel_config.pixels[count - self.length - 1] = COLORS[self.color_index]
        else:
            self.pixel_config.pixels[self.length] = COLORS[self.color_index]

        self.length += 1
        if self.length >= count:
            self.length = 0
            self.direction = -1 if random() > 0.5 else 1
            self.color_index = (self.color_index + 1) % len(COLORS)
