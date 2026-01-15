from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = now.strftime("app-%H_%M_%S.log")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(timestamp)
        print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
