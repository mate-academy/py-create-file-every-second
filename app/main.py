from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now().date()
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(f"{date} {hours}:{minutes}:{seconds}")

        print(
            f"{date} {hours}:{minutes}:{seconds}",
            f"app-{hours}_{minutes}_{seconds}.log"
        )

        sleep(1)


if __name__ == "__main__":
    main()
