import time
from bladerunner import Bladerunner
from fire2012 import Fire2012
from fadeout import Fadeout
from pixelconfig import PixelConfig

pixel_config = PixelConfig()

# flash blue as indication of successful startup
for i in range(pixel_config.count):
    pixel_config.pixels[i] = (50, 125, 200)
pixel_config.pixels.show()
time.sleep(0.5)

# list of patterns to cycle through
patterns = [
    Bladerunner(pixel_config),
    Fire2012(pixel_config),
]

# insert a Fadeout after every pattern
for i in range(len(patterns), 0, -1):
    patterns.insert(i, Fadeout(pixel_config))

frames = 0
pattern_index = 0
pattern = patterns[pattern_index]
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
