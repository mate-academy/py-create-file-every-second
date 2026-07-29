from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now: datetime = datetime.now()
        timestamp: str = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name: str = now.strftime("app-%H_%M_%S.log")

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")
        sleep(1)
