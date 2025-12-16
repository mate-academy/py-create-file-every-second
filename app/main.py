from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now: datetime = datetime.now()
        timestamp: str = now.strftime("%Y-%m-%d %H:%M:%S")
        filename: str = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(timestamp)

        print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
