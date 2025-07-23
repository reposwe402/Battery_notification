from pynotifier import Notification

def send_low_battery_notification(percent):
    Notification(
        title="Battery Low",
        description=f"{percent}% Battery remain!!",
        duration=5,  # Duration in seconds
    ).send()
