# handles data persistence, stores session info in a JSON file

import json
import os

class DataManager:
    def __init__(self, filename="pomodoro_data.json"):
        self.filename = filename
        self.data = self._load_data()

    # load data from file
    def _load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return {"sessions": []}

    # save to file
    def _save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f)

    # add session to data
    def add_session(self, study_time, break_time):
        self.data["sessions"].append({
            "study_time": study_time,
            "break_time": break_time
        })
        self._save_data()

    # get total study and break time data, for use in viewing stats in SessionManager
    def get_totals(self):
        total_study = sum(session["study_time"] for session in self.data["sessions"])
        total_break = sum(session["break_time"] for session in self.data["sessions"])
        return total_study, total_break