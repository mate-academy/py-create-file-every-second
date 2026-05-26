from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        time_stamp = (f"{now.year}-{now.month:02d}-{now.day:02d} "
                      f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}")

        with open(file_name, "w") as f:
            f.write(time_stamp)

        print(f"{time_stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
