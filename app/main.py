from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        filename = (
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(timestamp.strftime("%Y-%m-%d %H:%M:%S"))

        print(timestamp.strftime("%Y-%m-%d %H:%M:%S"), filename)

        sleep(1)


if __name__ == "__main__":
    main()
