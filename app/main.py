import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        now = now.replace(microsecond=0)
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as file:
            file.write(f"{now}")
        print(now, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
