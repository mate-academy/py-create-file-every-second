from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        timestamp = datetime.now()
        filename = (
            f"app-{timestamp.hour}_{timestamp.minute}"
            f"_{timestamp.second}.log"
        )

        with open(filename, "w") as f:
            f.write(str(timestamp))

        print(timestamp, filename)

        sleep(1)


if __name__ == "__main__":
    main()
