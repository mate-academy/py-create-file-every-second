from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        output_file = open(
            f"app-{time.hour}_{time.minute}_{time.second}.log", "w"
        )
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        output_file.write(timestamp)
        print(timestamp, f"app-{time.hour}_{time.minute}_{time.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
