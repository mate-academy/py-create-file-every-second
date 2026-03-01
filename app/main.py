from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        with open(f"app-{time_now.hour}_"
                  f"{time_now.minute}_"
                  f"{time_now.second}.log", "w") as input_file:
            input_file.write(f"{time_now}")

        with open(f"app-{time_now.hour}_"
                  f"{time_now.minute}_"
                  f"{time_now.second}.log", "r") as input_file:
            print(f"{input_file.read()} app-{time_now.hour}_"
                  f"{time_now.minute}_"
                  f"{time_now.second}.log"
                  )

        sleep(1)


if __name__ == "__main__":
    main()
