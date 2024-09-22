# SessionManager handles logic study and break timers, handles data with DataManager

from timer.study_timer import StudyTimer
from timer.break_timer import BreakTimer
from utils.data_manager import DataManager
import time

class SessionManager:
    def __init__(self):
        self.data_manager = DataManager()
        self.study_duration = 50 * 60  # default 50 min study period
        self.break_duration = 5 * 60   # default 5 min break period

    # session start
    def start_session(self):
        study_timer = StudyTimer(self.study_duration)
        break_timer = BreakTimer(self.break_duration)

        # start study timer
        print(f"Starting a study session for {self.study_duration // 60} minutes.")
        study_timer.start()
        self._run_timer(study_timer)
        study_timer.stop()

        # prompting to continue or quit
        user_input = input("Study session complete. Press 'Enter' to start break, 'q' to quit: ")
        if user_input.lower() == 'q':
            exit()
        
        # record focus score
        focus_score = int(input("Rate your focus during this session (1-5): "))
        study_timer.record_focus_score(focus_score)

        # start break timer
        print(f"Study session complete. Starting a break for {self.break_duration // 60} minutes.")
        break_timer.start()
        self._run_timer(break_timer)
        break_timer.stop()

        # break end, log sesh
        self._log_session(study_timer, break_timer)

    # running any timer
    def _run_timer(self, timer):
        # while session is running
        while not timer.is_complete():
            remaining = timer.duration - timer.get_elapsed_time()
            minutes, seconds = divmod(int(remaining), 60)

            # super useful prompt for timer type
            timer_type = timer.get_timer_type()
            
            # print cont log
            print(f"\r{timer_type} time remaining: {minutes:02d}:{seconds:02d}", end="", flush=True)
            time.sleep(1)

            # pause/resume functionality
            user_input = input("\nPress 'p' to pause, 'r' to resume, or 'Enter' to view time remaining: ")
            if user_input.lower() == 'p':
                timer.pause()
                print(f"{timer_type} timer paused. Press 'r' to resume.")
            elif user_input.lower() == 'r':
                timer.resume()
                print(f"{timer_type} timer resumed.")
        print(f"\n{timer_type} timer complete!")
    
    # logging session data
    def _log_session(self, study_timer, break_timer):
        study_time = study_timer.get_elapsed_time()
        break_time = break_timer.get_elapsed_time() if break_timer else 0
        focus_score = study_timer.get_focus_score()

        self.data_manager.add_session(study_time, break_time, focus_score)

    # for setting custom durations
    def set_durations(self, study_minutes, break_minutes):
        self.study_duration = study_minutes * 60
        self.break_duration = break_minutes * 60

    # for viewing total study and break time
    def view_stats(self):
        total_study, total_break, avg_focus = self.data_manager.get_totals()
        print(f"\nTotal study time: {total_study // 60} minutes")
        print(f"Total break time: {total_break // 60} minutes")
        print(f"Average focus score: {avg_focus:.2f}")
        print("\nRecent sessions:")
        for session in self.data_manager.get_recent_sessions(5):
            print(f"Study: {session['study_time']//60} min, Break: {session['break_time']//60} min, Focus score: {session['focus_score']:.2f}")