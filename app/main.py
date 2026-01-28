from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        dt = datetime.now()
        file_name = f"app-{dt.hour:02d}_{dt.minute:02d}_{dt.second:02d}.log"
        output_file = open(file_name, "w")
        output_file.write(
            f"{dt.year}-{dt.month:02d}-{dt.day:02d} "
            f"{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"
        )
        output_file.close()
        print(
            f"{dt.year}-{dt.month:02d}-{dt.day:02d} "
            f"{dt.hour:02d}:{dt.minute:02d}:{dt.second:02d} "
            f"{file_name}"
        )
        sleep(1)


if __name__ == "__main__":
    main()
