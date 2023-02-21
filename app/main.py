import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        file_name = (
            f"app-"
            f"{datetime.now().hour}_"
            f"{datetime.now().minute}_"
            f"{datetime.now().second}"
            f".log"
        )
        with open(file_name, "a") as f:
            timestamp = datetime.now()
            f.write(f"{timestamp}")
            print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
