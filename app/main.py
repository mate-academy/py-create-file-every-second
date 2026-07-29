from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{now.strftime('%H_%M_%S')}.log", "w") as f:
            f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {f.name}")
        sleep(1)


if __name__ == "__main__":
    main()
