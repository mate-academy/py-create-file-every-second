from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        time = datetime.now()
        with (open(f"app-{time.strftime(format="%H_%M_%S")}.log", "w")
              as logfile):
            logfile.write(f"{time.date()} {time.strftime(format="%H:%M:%S")}")
        print(f"{time.date()} {time.strftime(format="%H:%M:%S")} "
              f"{f"app-{time.strftime(format="%H_%M_%S")}.log"}")
        sleep(1)


if __name__ == "__main__":
    main()
