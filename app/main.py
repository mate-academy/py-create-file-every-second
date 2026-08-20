from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = str(now)
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
