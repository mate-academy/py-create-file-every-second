from datetime import datetime
import time


def main() -> None:
    while True:
        file_name = (
            f"app-{datetime.now().hour}"
            f"_{datetime.now().minute}"
            f"_{datetime.now().second}.log"
        )
        with open(file_name, "w") as f:
            f.write(f"{datetime.now()}")
            print(datetime.now(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
