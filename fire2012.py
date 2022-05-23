"""
Adapted from Fire2012 by Mark Kriegsman, July 2012
as part of "Five Elements" shown here: http://youtu.be/knWiGsmgycY

This basic one-dimensional 'fire' simulation works roughly as follows:
There's a underlying array of 'heat' cells, that model the temperature
at each point along the line.  Every cycle through the simulation,
four steps are performed:
 1) All cells cool down a little bit, losing heat to the air
 2) The heat from each cell drifts 'up' and diffuses a little
 3) Sometimes randomly new 'sparks' of heat are added at the bottom
 4) The heat from each cell is rendered as a color into the leds array
    The heat-to-color mapping uses a black-body radiation approximation.

Temperature is in arbitrary units from 0 (cold black) to 255 (white hot).

There are two main parameters you can play with to control the look and
feel of your fire: COOLING (used in step 1 above), and SPARKING (used
in step 3 above).
"""
import random

from pattern import Pattern
from util import lerp

# COOLING: How much does the air cool as it rises?
# Less cooling = taller flames.  More cooling = shorter flames.
# Default 55, suggested range 20-100
COOLING = 5

# SPARKING: What chance is there that a new spark will be lit?
# Higher chance = more roaring fire.  Lower chance = more flickery fire.
# Default 0.4, suggested range 0.2-0.8
SPARKING = 0.3

def heat_color(temperature):
    """
    Approximates a 'black body radiation' spectrum for
    a given 'heat' level.  This is useful for animations of 'fire'.
    Heat is specified as an arbitrary scale from 0 (cool) to 255 (hot).
    This is NOT a chromatically correct 'black body radiation'
    spectrum, but it's surprisingly close, and it's fast and small.
    """
    if temperature < 85:
        # Coolest third: ramp up red, no green, no blue
        heatramp = lerp(temperature, 0, 84, 0, 255)
        return heatramp, 0, 0
    elif temperature < 170:
        # Middle third: full red, ramp up green, no blue
        heatramp = lerp(temperature, 85, 169, 0, 255)
        return 255, heatramp, 0
    else:
        # Hottest third: full red, full green, ramp up blue
        heatramp = lerp(temperature, 170, 255, 0, 50)
        return 255, 255, heatramp


class Fire2012(Pattern):
    def initialize(self):
        super().initialize()

        # Array of temperature readings at each simulation cell. The fire starts unlit.
        # Values should be from 0 to 255
        self.heat = [0 for _ in range(self.pixel_config.count)]

    def progress(self):
        # Step 1.  Cool down every cell a little
        for i in range(self.pixel_config.count):
            cooling = random.randint(0, COOLING)
            # cooling = random.randint(0, round(COOLING * 10 / self.pixel_config.count) + 2)
            self.heat[i] = max(self.heat[i] - cooling, 0)

        # Step 2.  Heat from each cell drifts 'up' and diffuses a little
        for k in range(self.pixel_config.count - 1, 1, -1):
            self.heat[k] = round((self.heat[k - 1] + self.heat[k - 2]) / 2)
        self.heat[1] = self.heat[0]

        # Step 3.  Randomly ignite new 'sparks' of heat near the bottom
        if random.random() < SPARKING:
            y = random.randint(0, 7)
            spark_heat = random.randint(100, 255)
            self.heat[y] = min(self.heat[y] + spark_heat, 255)

        # Step 4.  Map from heat cells to LED colors
        for j in range(self.pixel_config.count):
            self.pixel_config.pixels[j] = heat_color(self.heat[j])
