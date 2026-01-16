from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(f"{datetime.now()}")
            print(datetime.now(), f"app-{hours}_{minutes}_{seconds}.log")
            sleep(1)
            continue


if __name__ == "__main__":
    main()
