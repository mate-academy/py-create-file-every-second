import time
from datetime import datetime


def main() -> None:
    while True:
        datetime_object = datetime.now()
        with open(f"app-{datetime_object.hour}_"
                  f"{datetime_object.minute}_"
                  f"{datetime_object.second}.log", "w") as f:
            f.write(str(datetime_object))
            print(datetime_object, f"app-{datetime_object.hour}_"
                                   f"{datetime_object.minute}_"
                                   f"{datetime_object.second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
