from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        datetime_now = datetime.now()
        with open(
                f"app-{datetime_now.hour}_"
                f"{datetime_now.minute}_"
                f"{datetime_now.second}.log", "w"
        ) as file:
            file.write(datetime_now.strftime("%Y-%m-%d %H:%M:%S"))
            print(
                datetime_now.strftime("%Y-%m-%d %H:%M:%S"),
                f"app-{datetime_now.hour}_"
                f"{datetime_now.minute}_"
                f"{datetime_now.second}.log"
            )
        sleep(1)


if __name__ == "__main__":
    main()
