# Perch LEDs

A personal LED project. Enjoy :)

## Hardware

- Raspberry Pi Pico (CircuitPython firmware)
- WS2812B LEDs (GPIO pin 0)
- Hardware button (GPIO pin 1)

## Development

Convenience script to copy python files to circuit python volume:

```zsh
./transfer
```

## To do

- Rather than fade out, do an interpolation between last frame of last pattern and first frame of next pattern
- Allow composition, for instance allow fading out an animated pattern
