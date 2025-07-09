from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        with open(
                f"app-{datetime.now().hour}_{datetime.now().minute}_"
                f"{datetime.now().second}.log", "w"
        ) as log_file:
            log_file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} "
              f"app-{datetime.now().hour}_{datetime.now().minute}_"
              f"{datetime.now().second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
