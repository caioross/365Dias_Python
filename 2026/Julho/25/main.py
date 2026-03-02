import psutil
import time
import os
import platform

def get_battery_percentage():
    """
    Returns the current battery percentage.
    """
    battery = psutil.sensors_battery()
    return battery.percent if battery else None

def play_sound():
    """
    Plays a sound notification.
    """
    if platform.system() == "Windows":
        os.system("start /min mplay32.exe *.wav")
    elif platform.system() == "Linux":
        os.system("aplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga")
    elif platform.system() == "Darwin":
        os.system("afplay /System/Library/Sounds/Glass.aiff")

def show_visual_notification(message):
    """
    Shows a visual notification with the given message.
    """
    print(f"\n\n{message}\n\n")

def monitor_battery():
    """
    Monitors the battery percentage and emits notifications when it reaches 20% or 80%.
    """
    while True:
        battery_percentage = get_battery_percentage()
        if battery_percentage is not None:
            if battery_percentage <= 20 or battery_percentage >= 80:
                play_sound()
                show_visual_notification(f"Battery level is at {battery_percentage}%")
        time.sleep(60)  # Check every minute

def main():
    """
    Main function to start the battery monitoring.
    """
    print("Battery monitor started. Press Ctrl+C to stop.")
    try:
        monitor_battery()
    except KeyboardInterrupt:
        print("Battery monitor stopped.")

if __name__ == '__main__':
    main()