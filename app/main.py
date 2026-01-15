from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        name = (
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"
        )

        with open(name, "w") as file:
            file.write(str(timestamp))

        print(f"{timestamp} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
