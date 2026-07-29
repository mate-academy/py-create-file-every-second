from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        file_name = (
            f"app-{now.hour:02}_"
            f"{now.minute:02}_"
            f"{now.second:02}.log"
        )
        time_stamp = (
            f"{now.year}-"
            f"{now.month:02}-"
            f"{now.day:02} "
            f"{now.hour:02}:"
            f"{now.minute:02}:"
            f"{now.second:02}"
        )
        with open(file_name, "w") as file:
            file.write(time_stamp)
        print(time_stamp + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
