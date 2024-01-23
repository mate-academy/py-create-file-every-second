import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        timestamp = str(current_time)
        with open(file_name, "w") as f:
            f.write(timestamp)
            print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
