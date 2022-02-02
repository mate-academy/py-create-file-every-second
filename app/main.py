import datetime
import time


def files_creator():
    while True:
        accurate_time = datetime.datetime.now()
        accurate_time = (f"app-{str(accurate_time.hour)}"
                         f"_{str(accurate_time.minute)}"
                         f"_{str(accurate_time.second)}.log")

        with open(accurate_time, "w") as f:
            f.write(str(datetime.datetime.now()))
            print(datetime.datetime.now(), accurate_time)
        time.sleep(1)


if __name__ == '__main__':
    files_creator()
