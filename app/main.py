import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        with open(
                f"app-{datetime.now().hour}"
                f"_{datetime.now().minute}"
                f"_{datetime.now().second}.log", "w"
        ) as file:
            file.write(f"{datetime.now()}")
            print(f"{datetime.now()} {file.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
