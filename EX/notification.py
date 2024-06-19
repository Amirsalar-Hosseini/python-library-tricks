from plyer import notification
import time
while True:
    notification.notify(
        title = "Its rest time",
        message = "Take a Break",
        timeout = 2
    )
    time.sleep(10)