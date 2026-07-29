from datetime import datetime
from time import sleep


def main() -> None:
    while True:

        current_time = datetime.now()
        filename = f"app-{current_time.strftime('%H_%M_%S')}.log"
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp)

        print(timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
