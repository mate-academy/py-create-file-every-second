from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        filename = (f"app-{timestamp.hour}"
                    f"_{timestamp.minute}"
                    f"_{timestamp.second}.log")
        with open(filename, "w") as file:
            file.write(f"{timestamp}")
            print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
