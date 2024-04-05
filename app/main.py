import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        filename = f"app-{hour:02d}_{minute:02d}_{second:02d}.log"
        with open(filename, "w") as file:
            file.write(str(now))
        with open(filename, "r") as file:
            print(file.read(), filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
