from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours = str(datetime.now())[11:13]
        minutes = str(datetime.now())[14:16]
        seconds = str(datetime.now())[17:19]
        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            f.write(str(datetime.now()))
            print(datetime.now(), f.name)
        sleep(1)


if __name__ == "__main__":
    main()
