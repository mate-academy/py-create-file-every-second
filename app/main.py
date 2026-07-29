from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time_now = datetime.now()
        file_name = ("app-" + str(date_time_now.hour) + "_"
                     + str(date_time_now.minute) + "_"
                     + str(date_time_now.second) + ".log")
        with open(file_name, "w") as f:
            f.write(str(date_time_now))
        print(str(date_time_now), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
