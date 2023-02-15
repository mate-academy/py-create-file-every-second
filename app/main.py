from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}"
                  f"_{now.second}.log", "w") as file:
            file.write(f"{now}")
            print(f"{now} app-{now.hour}_{now.minute}_{now.second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
