import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as file:
            file.write(str(now))
            print(str(now), filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
