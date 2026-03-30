from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        with open(
            f"app-{datetime.now().strftime('%H_%M_%S')}.log", "w"
        ) as file:
            file.write(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
        print(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} "
            f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        )
        sleep(1)


if __name__ == "__main__":
    main()
