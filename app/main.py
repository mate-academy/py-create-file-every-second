from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:

        now = datetime.now()

        with open(f"app-{now.hour}_{now.minute}_"
                  f"{now.second}.log", "w") as file_:
            file_.write(f"{now}")
            time.sleep(1)

        print(f"{now} app-{now.hour}_"
              f"{now.minute}_{now.second}.log")


if __name__ == "__main__":
    main()
