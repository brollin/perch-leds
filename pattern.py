class Pattern:
    # duration in seconds that pattern should run for
    duration = 4

    # when this boolean is true, pattern will be advanced regardless of duration shown
    finished = False

    def __init__(self, pixel_config) -> None:
            self.pixel_config = pixel_config
            self.fps = pixel_config.default_fps
            self.initialize()

    def initialize(self):
        self.finished = False

    def progress(self):
        pass
