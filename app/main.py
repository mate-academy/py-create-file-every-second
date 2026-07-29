import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        with open(f"app-{datetime.now().hour}_"
                  f"{datetime.now().minute}_"
                  f"{datetime.now().second}.log", "w+") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            file.seek(0)
            print(f"{file.read()} {file.name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
