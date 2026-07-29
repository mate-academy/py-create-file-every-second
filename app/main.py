from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.hour}_{now.minute}_{now.second}.log", "w") as f:
            f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")

        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')}"
              f" app-{now.hour}_{now.minute}_{now.second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
