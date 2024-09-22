# SessionManager handles study and break timers, handles data with DataManager

from ..timer.study_timer import StudyTimer
from ..timer.break_timer import BreakTimer
from ..utils.data_manager import DataManager

class SessionManager:
    def __init__(self):
        self.data_manager = DataManager()
        self.study_duration = 50 * 60  # default 50 min study period
        self.break_duration = 10 * 60   # default 10 min break period

    # session start
    def start_session(self):
        study_timer = StudyTimer(self.study_duration)
        break_timer = BreakTimer(self.break_duration)

        print(f"Starting a study session for {self.study_duration // 60} minutes.")
        study_timer.start()
        self._run_timer(study_timer)
        study_timer.stop()

        print(f"Study session complete. Starting a break for {self.break_duration // 60} minutes.")
        break_timer.start()
        self._run_timer(break_timer)
        break_timer.stop()

        self.data_manager.add_session(study_timer.get_elapsed_time(), break_timer.get_elapsed_time())

    # running any timer
    def _run_timer(self, timer):
        while not timer.is_complete():
            remaining = timer.duration - timer.get_elapsed_time()
            minutes, seconds = divmod(int(remaining), 60)
            print(f"\rTime remaining: {minutes:02d}:{seconds:02d}", end="", flush=True)
            time.sleep(1)
        print("\nTimer complete!")

    # for setting custom durations
    def set_durations(self, study_minutes, break_minutes):
        self.study_duration = study_minutes * 60
        self.break_duration = break_minutes * 60

    # for viewing total study and break time
    def view_stats(self):
        total_study, total_break = self.data_manager.get_totals()
        print(f"\nTotal study time: {total_study // 60} minutes")
        print(f"Total break time: {total_break // 60} minutes")