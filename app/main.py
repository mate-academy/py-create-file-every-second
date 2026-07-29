import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        with open(
                f"app-{now.hour}_{now.minute}_{now.second}.log", "w"
        ) as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(
            now.strftime("%Y-%m-%d %H:%M:%S"),
            f"app-{now.hour}_{now.minute}_{now.second}.log"
        )
        time.sleep(1)


if __name__ == "__main__":
    main()
