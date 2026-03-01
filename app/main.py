from datetime import datetime
import time


def main() -> None:

    while True:
        now = datetime.now()
        filename = f'app-{now.strftime("%H_%M_%S")}.log'
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as file:
            file.write(timestamp)

        print(timestamp, filename)

        time.sleep(1)
