from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = f"{now.hour:02}"
        minutes = f"{now.minute:02}"
        seconds = f"{now.second:02}"

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        current_time = str(now)[:19]

        with open(file_name, "w") as f:
            f.write(current_time)
        print(f"{current_time} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
