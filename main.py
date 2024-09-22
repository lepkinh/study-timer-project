# main python file (executable)

import time
from session.session_manager import SessionManager

def main():
    session_manager = SessionManager()

    # cheeky little menu in a while loop to prevent invalid inputs from crashing the program
    while True:
        print("\n--- Pomodoro Timer ---")
        print("1. Start a study session")
        print("2. Set custom durations")
        print("3. View stats")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            session_manager.start_session()

        elif choice == "2":
            study_minutes = int(input("Enter study duration in minutes: "))
            break_minutes = int(input("Enter break duration in minutes: "))
            session_manager.set_durations(study_minutes, break_minutes)

        elif choice == "3":
            session_manager.view_stats()

        elif choice == "4":
            print("FUCK OFFFF!!!!!")
            break
        
        # easter egg
        elif choice == "9":
            computer.explode()
        
        # invalid input catching
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()