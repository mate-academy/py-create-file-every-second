from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        with open(f"app-{hour}_{minute}_{second}.log", "w") as f:
            f.write(f"{year}-{month}-{day} {hour}:{minute}:{second}")
            print(f"{year}-{month}-{day} {hour}:{minute}:{second} "
                  f"app-{hour}_{minute}_{second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
