import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()

        filename = now.strftime("app-%H_%M_%S.log")
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp)
            print(f"{timestamp} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
