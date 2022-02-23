from datetime import datetime as d

import notify2
import pytz

tz_ist = pytz.timezone('Asia/Kolkata')
now_dt = d.now(tz_ist)
print(now_dt)
print(type(now_dt))
notification_dt = d(2021, 7, 16, 17, 1, 00, 00, tzinfo=tz_ist)
print(notification_dt)
print(type(notification_dt))
status_iwl = True

while now_dt > notification_dt or now_dt == notification_dt:
    now_dt = d.now(tz_ist)  # Update The Current Time Everytime The Loop Runs
    if status_iwl == True:
        print("In While Loop...")
        print()
        status_iwl = False
    print(f"Now : {now_dt}")
    print("  ")
    if now_dt == notification_dt:
        print("Activating Notification...")
        notify2.init('Critical Update')
        # TODO Add Iconb Path
        n = notify2.Notification(
            'Critical Update', '23 Packages Available')
        n.show()
        break


"""
while now_date == notification_dt.date and now_time < notification_dt.time or now_date.year == notification_dt.year and now_date.month == notification_dt.month and now_date.day == notification_dt.day and now_time.hour == notification_dt.hour and now_time.minute == notification_dt.minute:
    print("In while loop")
    if now_date.year == notification_dt.year and now_date.month == notification_dt.month and now_date.day == notification_dt.day and now_time.hour == notification_dt.hour and now_time.minute == notification_dt.minute:
        print("Activating...")
        notify2.init('Critical Update')
        iconPath = "/home/deathblade287/Pictures"
        n = notify2.Notification(
            'Critical Update', '23 Packages Available')
        n.show()
        break
"""
