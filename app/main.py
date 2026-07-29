# flake8: noqa
from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        the_time = datetime.now()
        file_name = f"app-{the_time.hour}_{the_time.minute}_{the_time.second}.log"
        time_stamp = f"{the_time.year}-{the_time.month}-{the_time.day} {the_time.hour}:{the_time.minute}:{the_time.second}"
        with open(file_name, "w") as file:
            file.write(time_stamp)
        print(f"{time_stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
