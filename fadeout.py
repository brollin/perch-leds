from pattern import Pattern
from util import dim

class Fadeout(Pattern):
    fps = 180
    dim_amount = 7

    def progress(self):
        self.finished = True
        for i in range(self.pixel_config.count):
            self.pixel_config.pixels[i] = dim(self.pixel_config.pixels[i], self.dim_amount)
            if sum(self.pixel_config.pixels[i]) > 0:
                self.finished = False
