from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = now.strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as f:
            f.write(formatted_time)

        print(f"{formatted_time} {file_name}")

        sleep(1)
