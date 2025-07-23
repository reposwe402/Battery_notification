from battery_status import get_battery_status
from notification import send_low_battery_notification

percent, plugged = get_battery_status()

if percent <= 30 and not plugged:
    send_low_battery_notification(percent)
