from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open(f"app-{datetime.now().strftime('%H')}_"
                  f"{datetime.now().strftime('%M')}_"
                  f"{datetime.now().strftime('%S')}.log", "a") as time_file:
            time_file.write(str(datetime.now()))
            print(str(datetime.now()) + f" app-{datetime.now().strftime('%H')}"
                  f"_{datetime.now().strftime('%M')}_"
                  f"{datetime.now().strftime('%S')}.log")
            time.sleep(1.0)


if __name__ == "__main__":
    main()
