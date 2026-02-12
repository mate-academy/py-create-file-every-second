from datetime import datetime
from time import sleep


def main() -> None:

    while True:

        time_now = datetime.now()

        file_name = (f"app-{time_now.hour}_"
                     f"{time_now.minute}_{time_now.second}.log")

        timestamp = time_now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
