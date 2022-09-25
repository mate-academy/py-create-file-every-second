from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(f"{datetime.now()}")
            print(datetime.now(), f"app-{hours}_{minutes}_{seconds}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
