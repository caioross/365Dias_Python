import psutil

def get_battery_info():
    """
    Retrieves the current battery percentage and charging status.

    Returns:
        tuple: A tuple containing the battery percentage and a boolean indicating if the charger is connected.
    """
    battery = psutil.sensors_battery()
    if battery is None:
        return None, None
    percent = battery.percent
    plugged = battery.power_plugged
    return percent, plugged

def main():
    """
    Main function to execute the battery monitoring script.
    """
    percent, plugged = get_battery_info()
    if percent is None:
        print("Battery information is not available.")
    else:
        print(f"Battery Percentage: {percent}%")
        print(f"Charger Connected: {'Yes' if plugged else 'No'}")

if __name__ == '__main__':
    main()