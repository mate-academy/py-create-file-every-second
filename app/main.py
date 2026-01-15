import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-7]
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
