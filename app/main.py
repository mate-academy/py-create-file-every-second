import time
from datetime import datetime


def main() -> None:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        hours, minutes, seconds = datetime.now().strftime("%H %M %S").split()
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {file_name}")

        time.sleep(1)


main()
