from datetime import datetime
import time


def main() -> None:
    while True:
        current = datetime.now()
        timestamp = current.strftime("%Y-%m-%d %H:%M:%S")
        hours = current.strftime("%H")
        mins = current.strftime("%M")
        seconds = current.strftime("%S")
        file_name = f"app-{hours}_{mins}_{seconds}.log"
        with open(file_name, "x") as file:
            file.write(timestamp)
        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
