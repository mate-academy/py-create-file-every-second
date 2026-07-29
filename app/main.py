import time
from datetime import datetime


def main() -> None:
    while True:
        text = open(
            f"app-{datetime.now().hour}_{datetime.now().minute}_"
            f"{datetime.now().second}.log", "w+"
        )
        text.write(f"{datetime.now()}")
        text.seek(0)
        print(f"{text.read()} {text.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
