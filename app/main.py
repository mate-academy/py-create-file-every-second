import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_date = datetime.now()
        log = (f"app-{current_date.hour}"
               f"_{current_date.minute}"
               f"_{current_date.second}"
               f".log")

        with open(log, "w") as file_log:

            file_log.write(str(current_date))
            print(current_date, log)
            time.sleep(1)


if __name__ == "__main__":
    main()
