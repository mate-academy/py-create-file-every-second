from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        timestamp = time_now.strftime("%Y-%m-%d %H:%M:%S")

        time_part = f"{time_now.hour}_{time_now.minute}_{time_now.second}"
        file_name = f"app-{time_part}.log"

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
