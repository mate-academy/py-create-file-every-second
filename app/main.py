from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date_time = str(datetime.now())
        my_time = date_time.split(" ")[1]
        hours, minutes, seconds = my_time.split(":")
        seconds = seconds.split(".")[0]
        name_file = f"app-{hours}_{minutes}_{seconds}.log"
        with open(name_file, "w") as datetime_file:
            datetime_file.write(date_time)
        print(date_time, name_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
