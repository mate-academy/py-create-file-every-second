from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now_ = datetime.now()
        filename = f"app-{now_.hour}_{now_.minute}_{now_.second}.log"
        with open(filename, "w", encoding="utf-8") as file:
            timestamp = now_.strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp)
        print(timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
