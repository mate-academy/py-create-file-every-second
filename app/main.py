from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = "app-{}_{}_{}.log".format(
            now.hour, now.minute, now.second
        )
        with open(filename, "w", encoding="utf-8") as file:
            file.write(timestamp)
        print(timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
