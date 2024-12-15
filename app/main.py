from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open(
            f"app-"
            f"{datetime.now().hour}_"
            f"{datetime.now().minute}_"
            f"{datetime.now().second}"
            f".log",
            "w"
        ) as new_file:
            new_file.write(str(datetime.now()))
            print(f"{datetime.now()} {new_file.name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
