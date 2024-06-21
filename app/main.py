from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour:02d}_{now.minute:02d}_{now.second:02d}.log"

        timestamp_str = now.strftime(f"{now.year}-{now.month:02d}-{now.day:02d} "
                                     f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}.{now.microsecond:06d}")

        with open(file_name, "w") as file:
            file.write(f"{timestamp_str}\n")

        print(f"{timestamp_str} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
