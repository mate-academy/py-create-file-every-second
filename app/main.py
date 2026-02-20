from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w", encoding="utf-8") as f:
            f.write(timestamp)

        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
