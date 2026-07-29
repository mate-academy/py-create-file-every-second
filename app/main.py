import time
from datetime import datetime


def main() -> None:
    while True:
        now = datetime.now()

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(timestamp)

            print(f"{timestamp} {file_name}")

        except OSError as e:
            print(f"Error creating file {file_name}: {e}")

        time.sleep(1)


if __name__ == "__main__":
    main()
