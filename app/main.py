from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        datetime_now = datetime.now().replace(microsecond=0)
        name_of_file = (f"app-{datetime_now.hour}_"
                        f"{datetime_now.minute}_{datetime_now.second}.log")
        with open(f"{name_of_file}", "w") as f:
            f.write(f"{datetime_now}")
        with open(f"{name_of_file}", "r") as f:
            print(f.read(), f.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
