import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w") as f:
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            f.write(timestamp)
            print(timestamp, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
