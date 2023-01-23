from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = (
            f"app-{datetime.now().hour}_"
            f"{datetime.now().minute}_"
            f"{datetime.now().second}.log"
        )
        with open(filename, "w+") as file:
            timestamp = (f"{datetime.now().date()} "
                         f"{datetime.now().time()}")
            file.write(timestamp)
            print(f"{timestamp} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
