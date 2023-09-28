import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date_now = datetime.now()
        with open(f"app-{date_now.hour}_{date_now.minute}_"
                  f"{date_now.second}.log", "w") as file:
            file.write(str(date_now))
            print(str(date_now) + " "
                  + f"app-{date_now.hour}_"
                    f"{date_now.minute}_{date_now.second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
