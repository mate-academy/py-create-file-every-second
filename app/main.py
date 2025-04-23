import time
from datetime import datetime


def main() -> None:
    while True:
        data_and_time = datetime.now()
        name_file = (f"app-{data_and_time.hour}_"
                     f"{data_and_time.minute}_"
                     f"{data_and_time.second}.log")
        with open(name_file, "w") as f:
            f.write(f"{data_and_time.date()} "
                    f"{data_and_time.strftime("%H:%M:%S")}")
            print(f"{data_and_time.date()} "
                  f"{data_and_time.strftime("%H:%M:%S")} {f.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
