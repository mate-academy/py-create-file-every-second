from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        today = datetime.now()
        file_name = (
            f"app-"
            f"{today.hour}_"
            f"{today.minute}_"
            f"{today.second}"
            f".log"
        )
        with open(file_name, "w") as file:
            print(str(today) + " " + file_name)
            file.write(str(today))
            sleep(1)


if __name__ == "__main__":
    main()
