from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = (
            f"{datetime.now().year}-"
            f"{datetime.now().month}-"
            f"{datetime.now().day} "
            f"{datetime.now().hour}:"
            f"{datetime.now().minute}:"
            f"{datetime.now().second}"
        )
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(current_time)

        print(f"{current_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
