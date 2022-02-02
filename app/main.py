import datetime
import time


def files_creator():
    while True:
        time_now = datetime.datetime.now()
        time_now = "app-" +\
                   str(time_now.hour) +\
                   "_" + str(time_now.minute) +\
                   "_" + str(time_now.second) +\
                   ".log"

        with open(time_now, "w") as f:
            f.write(str(datetime.datetime.now()))
            print(datetime.datetime.now(), time_now)
        time.sleep(1)


files_creator()
