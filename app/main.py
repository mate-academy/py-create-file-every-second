from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        file_name = current_time.strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
