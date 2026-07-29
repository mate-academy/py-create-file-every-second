from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = now.strftime("app-%H_%M_%S.log")
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp)
        print(timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
