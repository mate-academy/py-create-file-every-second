from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        logfile_name = (
            f"app-{datetime.now().hour}_"
            f"{datetime.now().minute}_"
            f"{datetime.now().second}.log"
        )
        with open(logfile_name, "wt") as file:
            file.write(str(datetime.now()))
        print(f"{datetime.now()} {logfile_name}")
        sleep(1)


if __name__ == "__main__":
    main()
