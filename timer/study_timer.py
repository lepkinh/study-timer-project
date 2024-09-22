# study timer, inherits BaseTimer

from .base_timer import BaseTimer

class StudyTimer(BaseTimer):
    def __init__(self, duration):
        super().__init__(duration)
        self.type = "Study"
    
    # recording how focused i am bc im trying to figure out optimal amt of time to study per block
    def record_focus(self, score):
        # 1-5 is simple but descriptive, not too much thought required to choose a score but gives good data
        if 1 <= score <= 5: 
            self.focus_score = score
        else:
            # trigger error if score is out of range
            # NOTE: considering replacing with except ValueError and replacing with a -1, then filter out all -1
            raise ValueError("Focus score must be from 1 and 5.")

    # read base_timer comment
    def get_timer_type(self):
        return "Study"