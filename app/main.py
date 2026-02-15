from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        filename = f"app-{now.strftime('%H_%M_%S')}.log"
        with open(filename, "a") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        print(now.strftime("%Y-%m-%d %H:%M:%S"), filename, end="")
        sleep(1)
        print()


if __name__ == "__main__":
    main()
