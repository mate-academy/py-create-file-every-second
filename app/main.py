from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        time_now = datetime.now()
        time_hour = time_now.hour
        time_minute = time_now.minute
        time_second = time_now.second
        file_name = f"app-{time_hour}_{time_minute}_{time_second}.log"
        file_opened = open(file_name, "w")
        file_opened.write(f"{time_now}")
        file_opened.close()
        print(f"{time_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
