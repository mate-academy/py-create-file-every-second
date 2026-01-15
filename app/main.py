from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        with open(f"app-{time_now.hour}_{time_now.minute}_"
                  f"{time_now.second}.log", "w") as file:
            file.write(f"{time_now}")
            print(time_now, file.name)
            time.sleep(1)


if __name__ == "__main__":
    main()
