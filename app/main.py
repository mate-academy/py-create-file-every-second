import datetime
import time


def files_creator():
    while True:
        accurate_time = datetime.datetime.now()
        file_name = (f"app-{str(accurate_time.hour)}"
                         f"_{str(accurate_time.minute)}"
                         f"_{str(accurate_time.second)}.log")

        with open(file_name, "w") as f:
            f.write(str(accurate_time))
            print(accurate_time, file_name)
        time.sleep(1)


if __name__ == '__main__':
    files_creator()
