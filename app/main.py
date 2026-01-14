from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        with (open(f"app-{time.hour}_{time.minute}_{time.second}.log", "w")
              as f):
            f.write(str(time))
        print(time, f"app-{time.hour}_{time.minute}_{time.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
