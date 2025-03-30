import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    def file_creation() -> None:
        file_name = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_{datetime.now().second}.log")
        with open(file_name, "a") as f:
            f.write(f"{datetime.now()}")
        with open(file_name, "r") as f:
            print(f.read(), file_name)

    while True:
        file_creation()
        time.sleep(1)


if __name__ == "__main__":
    main()
