from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open(
            f"app-{datetime.now().hour}_{datetime.now().minute}"
            f"_{datetime.now().second}.log",
            "w",
        ) as e:
            e.write(f"{datetime.now()}")
            print(
                datetime.now(),
                f"app-{datetime.now().hour}_{datetime.now().minute}"
                f"_{datetime.now().second}.log",
            )
        time.sleep(1)


if __name__ == "__main__":
    main()
