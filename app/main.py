from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        timestamp = datetime.now()
        filename = \
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"

        with open(filename, "w") as f:
            f.write(str(timestamp))

        print(timestamp, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
