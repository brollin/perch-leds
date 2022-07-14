class Pattern:
    # duration in seconds that pattern should run for
    duration = 60 * 10

    # when this boolean is true, pattern will be advanced regardless of duration shown
    finished = False

    def __init__(self, pixel_config) -> None:
            self.pixel_config = pixel_config
            self.fps = pixel_config.default_fps
            self.initialize()

    def initialize(self):
        self.finished = False

    def progress(self):
        raise NotImplemented

    @property
    def total_frames(self):
        return self.duration * self.fps
