import psutil

def get_battery_status():
    battery = psutil.sensors_battery()
    return battery.percent, battery.power_plugged
