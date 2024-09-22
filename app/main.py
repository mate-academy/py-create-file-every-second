import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        timestamp = datetime.now()
        file_name = \
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"
        with open(file_name, "w") as file:
            file.write(str(timestamp))

        print(f"{timestamp} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
