from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now: datetime = datetime.now()
        timestamp_str: str = now.strftime("%Y-%m-%d %H:%M:%S")
        filename: str = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w") as file:
            file.write(timestamp_str)

        print(f"{timestamp_str} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
