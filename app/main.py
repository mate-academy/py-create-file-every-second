import time
from datetime import datetime


def main() -> None:

    while True:

        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(
                f"app-{now.hour}_{now.minute}_{now.second}.log", "a"
        ) as file:
            file.write(formatted_now)
            print(f"{formatted_now} {file.name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
