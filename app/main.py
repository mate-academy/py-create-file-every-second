import datetime
import time

while True:
    timestamp = datetime.datetime.now().strftime("%H_%M_%S")

    with open("app-" + timestamp + ".log", "w") as f:
        f.write(str(datetime.datetime.now()))
        print(str(datetime.datetime.now()), "app-" + timestamp + ".log")
        time.sleep(1)
