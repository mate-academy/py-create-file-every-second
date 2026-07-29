from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        timestamp_string = str(timestamp)
        filename = (
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"
        )

        with open(filename, "w") as file:
            file.write(timestamp_string)

        print(f"{timestamp_string} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
