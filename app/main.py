from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now: datetime = datetime.now()
        filename: str = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp: str = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
