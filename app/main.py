from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        data_now = datetime.now()
        with open(f"app-{data_now.hour}_{data_now.minute}_"
                  f"{data_now.second}.log", "w") as file_date:
            print(f"{data_now} app-{data_now.hour}_"
                  f"{data_now.minute}_{data_now.second}.log")
            file_date.write(f"{data_now}")
        sleep(1)


if __name__ == "__main__":
    main()
