from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        filename = current_time.strftime("app-%H_%M_%S.log")

        with open(filename, mode="w") as file:
            file.write(timestamp)

        print(f"{timestamp} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
