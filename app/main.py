from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_and_time_now = str(datetime.now())
        hours = date_and_time_now[11:13]
        minutes = date_and_time_now[14:16]
        seconds = date_and_time_now[17:19]
        name_of_file = f"app-{hours}_{minutes}_{seconds}.log"
        with open(name_of_file, "w") as current_log:
            current_log.write(date_and_time_now)
        print(f"{date_and_time_now} {name_of_file}")
        sleep(1)


if __name__ == "__main__":
    main()
