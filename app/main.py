from datetime import datetime
import time


def main() -> None:
    while True:
        timestamp = datetime.now()
        with open(
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log",
            "w",
        ) as file:
            file.write(timestamp.strftime("%Y-%m-%d %H:%M:%S"))
            print(timestamp.strftime("%Y-%m-%d %H:%M:%S"), file.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
