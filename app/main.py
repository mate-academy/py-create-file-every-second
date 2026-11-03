from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp = f"{now:%Y-%m-%d %H:%M:%S}"

        with open(filename, "a") as file:
            file.write(f"{timestamp}")
            print(f"{timestamp} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
