from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        with open(
            f"app-{hour}_{minute}_{second}.log", "w", encoding="utf-8"
        ) as file:
            file.write(f"{now}")
        with open(
            f"app-{hour}_{minute}_{second}.log", "r", encoding="utf-8"
        ) as file:
            print(f"{file.read()} {file.name}")
        sleep(1)


if __name__ == "__main__":
    main()
