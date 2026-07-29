from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (
            f"app-{current_time.hour}_"
            f"{current_time.minute}_"
            f"{current_time.second}.log"
        )
        file_line = (
            f"{current_time.year}-"
            f"{current_time.month}-"
            f"{current_time.day} "
            f"{current_time.hour}:"
            f"{current_time.minute}:"
            f"{current_time.second}"
        )
        with open(file_name, "w") as f:
            f.write(file_line)
            print(file_line, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
