from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_to_be_created = open(
            f"app-{datetime.now().hour}_"
            f"{datetime.now().minute}_{datetime.now().second}.log", "w")

        timestamp_to_write = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_to_be_created.write(f"{timestamp_to_write}")
        print(f"{timestamp_to_write} {file_to_be_created.name}")
        sleep(1)


if __name__ == "__main__":
    main()
