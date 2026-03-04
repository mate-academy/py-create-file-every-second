from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(str(now))

        print(now, file_name)

        sleep(1)
