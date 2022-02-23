# import time

# import notify2

# # from topnews import topStories

# # path to notification window icon
# # ICON_PATH =

# # fetch news items
# newsitems = "try"

# # initialise the d-bus connection
# notify2.init("News Notifier")

# # create Notification object
# # n = notify2.Notification(None, icon=ICON_PATH)
# n = notify2.Notification(None)

# # set urgency level
# n.set_urgency(notify2.URGENCY_NORMAL)

# # set timeout for a notification
# n.set_timeout(10000)

# # for newsitem in newsitems:

# #     # update notification data for Notification object
# #     n.update(newsitem['title'], newsitem['description'])

# #     # show notification on screen
# #     n.show()

# #     # short delay between notifications
# #     time.sleep(15)

# # import Notify2

# # Notify2.init("App Name")
# # Notify2.Notification.new("Hi").show()

from datetime import datetime as d

import notify2

now = d.now()
now_date = now.date()
now_time = now.time()
print(now)
print(type(now))
notification_time = d(2021, 7, 14, 19, 18, 00, 00, None)
print(notification_time)
print(type(notification_time))

while now_date == notification_time.date and now_time < notification_time.time or now_date.year == notification_time.year and now_date.month == notification_time.month and now_date.day == notification_time.day and now_time.hour == notification_time.hour and now_time.minute == notification_time.minute:
    print("In while loop")
    if now_date.year == notification_time.year and now_date.month == notification_time.month and now_date.day == notification_time.day and now_time.hour == notification_time.hour and now_time.minute == notification_time.minute:
        print("Activating...")
        notify2.init('Critical Update')
        iconPath = "/home/deathblade287/Pictures"
        n = notify2.Notification(
            'Critical Update', '23 Packages Available')
        n.show()
        break
