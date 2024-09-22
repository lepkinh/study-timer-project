# break timer, inherits BaseTimer

from .base_timer import BaseTimer

class BreakTimer(BaseTimer):
    def __init__(self, duration):
        super().__init__(duration)
        self.type = "Break"