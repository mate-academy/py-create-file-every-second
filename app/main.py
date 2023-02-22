from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        with open(
                f"app-{datetime.now().strftime('%H')}"
                f"_{datetime.now().strftime('%M')}"
                f"_{datetime.now().strftime('%S')}.log",
                "w"
        ) as f:
            f.write(str(datetime.now()))
            print(str(datetime.now()) + " " + f.name)
            sleep(1)


if __name__ == "__main__":
    main()
