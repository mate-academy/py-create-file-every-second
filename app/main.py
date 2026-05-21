from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        file_name = f"app-{hour}_{minute}_{second}.log"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "a") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
