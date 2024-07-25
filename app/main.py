from datetime import datetime
import time


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_{datetime.now().minute}"
                     f"_{datetime.now().second}.log")
        with open(file_name, "w") as f:
            f.write(f"{datetime.now()}")
            time.sleep(1)
        with open(file_name, "r") as f:
            print(f"{f.read()} {file_name}")


if __name__ == "__main__":
    main()
