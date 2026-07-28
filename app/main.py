import time
from datetime import datetime


def main() -> None:
    while True:
        with open(
                "app-"
                + datetime.now().strftime("%H_%M_%S")
                + ".log", "w"
        ) as file:
            file.write(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            print(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                file.name
            )
        time.sleep(1)


if __name__ == "__main__":
    main()
