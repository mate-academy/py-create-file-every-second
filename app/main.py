import datetime
import time


def logs():
    while True:
        currenttime = datetime.datetime.now()
        hours = currenttime.hour
        minutes = currenttime.minute
        seconds = currenttime.second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "a") as f:
            f.writelines(f"{currenttime}")
        with open(f"app-{hours}_{minutes}_{seconds}.log", "r") as f:
            print(f"{f.read()} app-{hours}_{minutes}_{seconds}.log")
        time.sleep(1)
