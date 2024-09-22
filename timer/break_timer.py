# break timer, inherits BaseTimer

from timer.base_timer import BaseTimer

class BreakTimer(BaseTimer):
    def __init__(self, duration):
        super().__init__(duration)
        self.type = "Break"

    # read base_timer comment
    def get_timer_type(self):
        return "Break"