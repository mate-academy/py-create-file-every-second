from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        time1 = datetime.now()
        timestamp = time1.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{time1.hour}_{time1.minute}_{time1.second}.log"

        with open(file_name, "w") as f:
            f.write(timestamp)

        print(timestamp, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
