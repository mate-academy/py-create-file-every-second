from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        filename = (
            f"app-{current_time.hour}_{current_time.minute}_"
            f"{current_time.second}.log"
        )

        with open(filename, "w") as file:
            file.write(timestamp)

        print(timestamp, filename)
        sleep(1)


if __name__ == "__main__":
    main()
