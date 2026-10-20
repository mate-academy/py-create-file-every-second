from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with (open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w")
              as log_file):
            log_file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(now.strftime("%Y-%m-%d %H:%M:%S"),
              f"app-{now.hour}_{now.minute}_{now.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
