from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (f"app-{time_now.hour}_"
                     f"{time_now.minute}_{time_now.second}.log")
        file_second = open(file_name, "w")
        file_second.write(str(time_now))
        print(str(time_now) + " " + file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()

# t = datetime.now()
#
# print(t)
# time.sleep(1)
# print(datetime.now())
