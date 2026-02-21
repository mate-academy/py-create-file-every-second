from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "a") as f:
            f.write(f"{datetime.now()}")
            print(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                f" {file_name}"
            )
        sleep(1)
