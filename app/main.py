from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")
        time.sleep(1)
