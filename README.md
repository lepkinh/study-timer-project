# Study Timer

Study Timer is a Python-based application designed to help users manage their study sessions effectively. This program was created to view my own study data and because most study apps are overengineered, they take too much time to interact with and setup, and this takes time away from studying. 
Made as a submission for the Solar Car design team application.

## Features

- Customizable study and break durations
- Pause and resume functionality for timers
- Focus score tracking for each study session
- Session statistics viewing
- Data persistence using JSON

## Project Structure

- `main.py`: The main executable file containing the user interface.
- `session/session_manager.py`: Manages study sessions and breaks.
- `timer/base_timer.py`: Base class for timers.
- `timer/study_timer.py`: Timer specific to study sessions.
- `timer/break_timer.py`: Timer specific to break sessions.
- `utils/data_manager.py`: Handles data persistence and statistics.

## How to Use

1. Run `main.py` to start the application.
2. Choose from the following options:
   - Start a study session
   - Set custom durations for study and break periods
   - View statistics of your study sessions
   - Exit the application

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/lepkinh/study-timer-project.git
   ```
2. Navigate to the project directory:
   ```
   cd study-timer-project
   ```
3. Run the main script:
   ```
   py main.py
   ```

## Requirements

- Python 3.6 or higher

## License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.