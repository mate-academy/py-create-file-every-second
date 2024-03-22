from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        with open(f"app-{current_date.hour}_"
                  f"{current_date.minute}_"
                  f"{current_date.second}.log", "a+") as f:

            f.write(f"{current_date}")
            f.seek(0)
            print(f"{f.read()} {f.name}")
        sleep(1)
