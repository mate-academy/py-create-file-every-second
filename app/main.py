from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        with open(
                f"app-{now.hour}_"
                f"{now.minute}_"
                f"{now.second}.log", "w"
        ) as file:
            file.write(str(now))

        print(now, f"app-{now.hour}_{now.minute}_{now.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
