from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        file_name = f"app-{current_date.strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as f:
            f.write(current_date.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"{current_date} {file_name}")
        sleep(1)
