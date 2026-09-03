from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = current_time.strftime("app-%H_%M_%S.log")
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w") as file:
            file.write(timestamp)
        print(timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
