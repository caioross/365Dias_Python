import time
import os

def play_sound():
    """Plays a sound using the terminal's bell character."""
    print("\a")

def timer(duration, message):
    """
    Starts a timer for the given duration and prints a message when done.

    :param duration: Time in seconds for the timer.
    :param message: Message to print when the timer is done.
    """
    while duration:
        mins, secs = divmod(duration, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        duration -= 1
    print(message)
    play_sound()

def pomodoro_cycle():
    """Runs a single Pomodoro cycle: 25 minutes of focus, followed by a 5-minute break."""
    print("Starting Pomodoro cycle...")
    timer(25 * 60, "Time to take a break!")
    timer(5 * 60, "Break's over, back to work!")

def main():
    """Main function to run multiple Pomodoro cycles."""
    cycles = int(input("How many Pomodoro cycles would you like to do? "))
    for _ in range(cycles):
        pomodoro_cycle()
    print("Pomodoro session completed!")

if __name__ == '__main__':
    main()