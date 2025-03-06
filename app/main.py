import time
from datetime import datetime


def main() -> None:
    while True:

        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
