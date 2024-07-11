from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        with open(
                f"app-{datetime.now().hour}_"
                f"{datetime.now().minute}_"
                f"{datetime.now().second}.log", "a"
        ) as f:
            f.write(f"{datetime.now()}")
        print(datetime.now(), f.name)
        sleep(1)
        continue


if __name__ == "__main__":
    main()
