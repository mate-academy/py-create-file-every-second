from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp = (f"{current_time.year}-"
                     f"{str(current_time.month).zfill(2)}-"
                     f"{str(current_time.day).zfill(2)}"
                     f" {str(current_time.hour).zfill(2)}"
                     f":{str(current_time.minute).zfill(2)}"
                     f":{str(current_time.second).zfill(2)}")
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        with open(file_name, "w") as f:
            f.write(timestamp)
        print(timestamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
