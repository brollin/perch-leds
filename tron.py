from random import random
from pattern import Pattern
from util import lerp3

TEAL = (19, 241, 242)
# BLUE = (59, 94, 166)
PURPLE = (115, 21, 114)
# MAGENTA = (192, 0, 80)
RED = (255, 38, 54)
YELLOW = (255, 170, 26)
COLORS = [TEAL, PURPLE, RED, YELLOW]

class Tron(Pattern):
    fps = 60

    def initialize(self):
        super().initialize()

        self.color_index = 3
        self.length = 0
        self.direction = -1 if random() > 0.5 else 1
        self.transition = 0.2 * self.pixel_config.count

    def progress(self):
        count = self.pixel_config.count
        color = COLORS[self.color_index]
        for i in range(count):
            if self.direction == 1:
                last_color = self.pixel_config.pixels[count - 1]
                if i < self.length - self.transition:
                    self.pixel_config.pixels[i] = color
                elif i < self.length:
                    self.pixel_config.pixels[i] = lerp3(i, self.length - self.transition, self.length, color, last_color)
            else:
                last_color = self.pixel_config.pixels[0]
                if i < self.length - self.transition:
                    self.pixel_config.pixels[count - i - 1] = color
                elif i < self.length:
                    self.pixel_config.pixels[count - i - 1] = lerp3(i, self.length - self.transition, self.length, color, last_color)

        self.length += 1
        if self.length >= count + self.transition:
            self.length = 0
            self.direction = -1 if random() > 0.5 else 1
            # select new random color
            self.color_index = (self.color_index + 1 + round(random() * (len(COLORS) - 2))) % len(COLORS)
