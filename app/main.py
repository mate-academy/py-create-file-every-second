import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()
        current_file = open(
            f"app-{now.hour}_{now.minute}_{now.second}.log", "w"
        )
        print(now, current_file.name)
        current_file.write(f"{now}")
        current_file.close()
        time.sleep(1)


if __name__ == "__main__":
    main()
