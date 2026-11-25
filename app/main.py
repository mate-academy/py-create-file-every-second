from datetime import datetime

from time import sleep


def main() -> None:
    while True:
        moment = datetime.now()
        file_name = f"app-{moment.hour}_{moment.minute}_{moment.second}.log"
        timestamp = moment.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(timestamp)
        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
