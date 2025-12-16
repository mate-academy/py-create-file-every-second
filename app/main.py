from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.strftime('%H_%M_%S')}.log", "w") as file:
            file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} "
              f"app-{now.strftime('%H_%M_%S')}.log")
        sleep(1)


if __name__ == "__main__":
    main()
