# base class for timers, common functionality

import time

class BaseTimer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def get_elapsed_time(self):
        if self.start_time is None:
            return 0
        if self.end_time is None:
            return time.time() - self.start_time
        return self.end_time - self.start_time

    def is_complete(self):
        return self.get_elapsed_time() >= self.duration