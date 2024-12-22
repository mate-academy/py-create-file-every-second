from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        extention = ".log"
        app = "app-"
        current_time = datetime.now()
        with open(f"{app}{current_time.hour}"
                  f"_{current_time.minute}"
                  f"_{current_time.second}"
                  f"{extention}", "w"
                  ) as f:
            f.write(str(datetime.now()))
            print(datetime.now(), f.name)
            sleep(1)


if __name__ == "__main__":
    main()
