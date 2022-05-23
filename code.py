import time
from bladerunner import Bladerunner
from fire2012 import Fire2012
from fadeout import Fadeout
from pixelconfig import PixelConfig
from tron import Tron

pixel_config = PixelConfig()

# flash blue as indication of successful startup
for i in range(pixel_config.count):
    pixel_config.pixels[i] = (50, 125, 200)
pixel_config.pixels.show()
time.sleep(0.5)

# list of patterns to cycle through
patterns = [
    Tron(pixel_config),
    Bladerunner(pixel_config),
    Fire2012(pixel_config),
]

# insert a Fadeout after every pattern
for i in range(len(patterns), 0, -1):
    patterns.insert(i, Fadeout(pixel_config))

pattern_index = 0
pattern = patterns[pattern_index]
while True:
    # display frames of pattern until finished
    for _ in range(pattern.total_frames):
        if pattern.finished:
            break

        pattern.progress()
        pixel_config.pixels.show()
        time.sleep(1 / pattern.fps)

    # advance pattern
    pattern_index = (pattern_index + 1) % len(patterns)
    pattern = patterns[pattern_index]
    pattern.initialize()
