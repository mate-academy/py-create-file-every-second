from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time1 = datetime.now()
        with open(f"app-{time1.hour}_{time1.minute}_"
                  f"{time1.second}.log", "w") as f:
            f.write(f"{time1}")
            print(time1, f"app-{time1.hour}_{time1.minute}_{time1.second}.log")
            sleep(1)


if __name__ == "__main__":
    main()
