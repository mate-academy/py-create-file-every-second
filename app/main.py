from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}"
                     f"_{datetime.now().minute}"
                     f"_{datetime.now().second}.log")
        timestamp = str(datetime.now())

        with open(file_name, "w", newline="") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
