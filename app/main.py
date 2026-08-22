from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        name = (f"app-"
                f"{date.hour}_"
                f"{date.minute}_"
                f"{date.second}"
                f".log")
        timestamp = (f""
                     f"{date.year}-"
                     f"{date.month}-"
                     f"{date.day} "
                     f"{date.hour}:"
                     f"{date.minute}:"
                     f"{date.second}"
                     f"")

        with open(name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {name}")

        sleep(1)


if __name__ == "__main__":
    main()
