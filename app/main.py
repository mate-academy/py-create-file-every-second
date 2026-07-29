from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        time_object = datetime.now().time()
        hours = time_object.hour
        minutes = time_object.minute
        seconds = time_object.second

        log = f"{current_date} app-{hours}_{minutes}_{seconds}.log"

        with open(f"app-{hours}_{minutes}_{seconds}.log", "a") as f:
            f.write(f"{current_date}")
            print(log)

        sleep(1)


if __name__ == "__main__":
    main()
