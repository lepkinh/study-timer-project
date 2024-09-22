# base class for timers, common functionality

import time

class BaseTimer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None
        self.end_time = None
        self.paused_time = 0
        self.is_paused = False

    # start timer
    def start(self):
        self.start_time = time.time()

    # stop timer
    def stop(self):
        self.end_time = time.time()

    # pause timer
    def pause(self):
        if not self.is_paused:
            self.is_paused = True
            self.paused_time += time.time() - (self.start_time + self.paused_time)

    # resume timer
    def resume(self):
        if self.is_paused:
            self.is_paused = False
            self.paused_time = time.time() - (self.start_time + self.paused_time)

    # get passed time
    def get_elapsed_time(self):
        # if timer hasnt begun
        if self.start_time is None:
            return 0

        # if timer is paused
        if self.is_paused:
            return self.paused_time

        # if timer is running, calculate time passed since beginning factoring in paused time
        if self.end_time is None:
            return time.time() - self.start_time - self.paused_time
        return self.end_time - self.start_time - self.paused_time

    # check if timer is complete
    def is_complete(self):
        return self.get_elapsed_time() >= self.duration

    # return timer name, not needed for base timer actually but its here for organization might remove
    def get_timer_type(self):
        return "Base"