from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = datetime.now().strftime("app-%H_%M_%S.log")

        with open(filename, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
