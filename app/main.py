from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.strftime("%H_%M_%S")}.log"

        with open(filename, "w") as file:
            file.write(timestamp)

        print(timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
