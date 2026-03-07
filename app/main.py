from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        name = datetime.now().strftime("app-%H_%M_%S.log")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(name, "w") as f:
            f.write(f"{timestamp}")
        print(f"{timestamp} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
