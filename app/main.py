from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        with open(
                f"app-{datetime.now().hour}_"
                f"{datetime.now().minute}_{datetime.now().second}.log",
                "w+"
        ) as f:
            f.write(str(datetime.now()))
            f.seek(0)
            print(f.read(), f.name)
            sleep(1)


if __name__ == "__main__":
    main()
