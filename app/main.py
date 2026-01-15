from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # write your code here
    while True:
        time_writ = datetime.now()
        with open(f"app-{time_writ.hour}_"
                  f"{time_writ.minute}_{time_writ.second}.log", "w") as f:
            f.write(f"{time_writ}")
        print(f"{time_writ} app-{time_writ.hour}_"
              f"{time_writ.minute}_{time_writ.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
