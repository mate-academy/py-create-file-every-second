import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        with open(
                f"app-{now.hour}_{now.minute}_{now.second}.log", "a"
        ) as file:
            file.write(
                f"{now.date()} {now.hour}:{now.minute}:{now.second}"
            )
            print(
                f"{now.date()} {now.hour}:{now.minute}:{now.second} "
                f"app-{now.hour}_{now.minute}_{now.second}.log"
            )
        time.sleep(1)


if __name__ == "__main__":
    main()
