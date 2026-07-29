from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        filename: str = (
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"
        )
        formatted_timestamp: str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w") as fobj:
            fobj.write(formatted_timestamp)
        print(f"{formatted_timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
