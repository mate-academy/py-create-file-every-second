from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        with open(f"app-{current_time.hour}_"
                  f"{current_time.minute}_"
                  f"{current_time.second}.log", "w") as f:
            f.write(str(current_time))
            print(f"{str(current_time)} "
                  f"app-{current_time.hour}_"
                  f"{current_time.minute}_"
                  f"{current_time.second}.log")
            sleep(1)


if __name__ == "__main__":
    main()
