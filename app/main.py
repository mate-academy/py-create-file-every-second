from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = now.strftime("%H_%M_%S")
        with open(f"app-{filename}.log", "w") as f:
            f.write(f"{now}")
            print(f"{now} app-{filename}.log")
        sleep(1)


if __name__ == "__main__":
    main()
