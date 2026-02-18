from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            timestamp = str(datetime.now())
            f.write(timestamp)
            print(f"{timestamp} app-{hours}_{minutes}_{seconds}.log")

        sleep(1)


if __name__ == "__main__":
    main()
