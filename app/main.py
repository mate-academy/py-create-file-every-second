from datetime import datetime
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as file:
            timestamp = datetime.now()
            file.write(f"{timestamp}")
            print(timestamp, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
