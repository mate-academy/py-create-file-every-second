from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        hours = current_date.hour
        minutes = current_date.minute
        seconds = current_date.second

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
            file.write(str(current_date))
            print(current_date, f"app-{hours}_{minutes}_{seconds}.log")

        sleep(1)


if __name__ == "__main__":
    main()
