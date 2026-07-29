from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        filename = f"app-{timestamp.hour}_{timestamp.minute}_"
        filename += f"{timestamp.second}.log"
        with open(filename, "w") as f:
            print(timestamp, filename)
            f.write(str(timestamp))
        sleep(1)


if __name__ == "__main__":
    main()
