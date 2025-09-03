from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        with open(f"app-{current_time.hour}_{current_time.minute}"
                  f"_{current_time.second}.log", "w") as file:
            file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{current_time} app-{current_time.hour}_"
                  f"{current_time.minute}"
                  f"_{current_time.second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
