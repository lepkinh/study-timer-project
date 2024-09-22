# study timer, inherits BaseTimer

from .base_timer import BaseTimer

class StudyTimer(BaseTimer):
    def __init__(self, duration):
        super().__init__(duration)
        self.type = "Study"