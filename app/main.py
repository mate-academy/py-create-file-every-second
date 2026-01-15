from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open(
                f"app-{datetime.now().hour}_{datetime.now().minute}_"
                f"{datetime.now().second}.log", "w"
        ) as f:
            print(
                datetime.now(),
                f"app-{datetime.now().hour}_{datetime.now().minute}_"
                f"{datetime.now().second}.log"
            )
            f.write(str(datetime.now()))
        time.sleep(1)


if __name__ == "__main__":
    main()
