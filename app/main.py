from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_now = datetime.now()
        with open(
                f"app-{date_now.hour}_{date_now.minute}_{date_now.second}.log",
                "a+"
        ) as f:
            f.write(str(datetime.now()))
        with open(
                f"app-{date_now.hour}_{date_now.minute}_{date_now.second}.log",
                "r"
        ) as f:
            print(f"{f.read()} {f.name}")
        sleep(1)


if __name__ == "__main__":
    main()
