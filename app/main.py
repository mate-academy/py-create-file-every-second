from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        current_datetime = datetime.now()
        filename = (
            f"app-{current_datetime.hour}_"
            f"{current_datetime.minute}_"
            f"{current_datetime.second}.log"
        )

        with open(filename, "w+") as file:
            file.write(f"{current_datetime}")

        print(f"{current_datetime} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
