from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        now_time = str(datetime.now())
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as log_file:
            log_file.write(now_time)

        print(f"{now_time} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
