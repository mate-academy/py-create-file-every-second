from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(name, "w") as f:
            f.write(str(now))

        print(f"{str(now)} {name}")
        time.sleep(1)
