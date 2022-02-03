import datetime
import time


def files_creator():
    while True:
        time_now = datetime.datetime.now()
        new_file_name = "app-" +\
            str(time_now.hour) +\
            "_" + str(time_now.minute) +\
            "_" + str(time_now.second) +\
            ".log"

        with open(new_file_name, "w") as f:
            f.write(str(time_now))
            print(time_now, new_file_name)
        time.sleep(1)


files_creator()
