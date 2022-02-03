import datetime
import time


def logs():
    while True:
        currenttime = datetime.datetime.now()
        name = f"app-{currenttime.strftime('%H_%M_%S')}.log"
        with open(name, "a") as f:
            f.writelines(str(currenttime))
        print(currenttime, name)
        time.sleep(1)
