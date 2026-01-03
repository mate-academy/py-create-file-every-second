from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(timestamp)

        print(timestamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
