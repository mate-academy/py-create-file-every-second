from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(timestamp_str)  # Без \n

        print(f"{timestamp_str} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
