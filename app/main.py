from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = (
            f"app-{now.hour:02}_"
            f"{now.minute:02}_"
            f"{now.second:02}.log"
        )
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(date_time)
            print(f"{date_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
