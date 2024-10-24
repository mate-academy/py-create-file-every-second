from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_{current_time.minute}_"
                     f"{current_time.second}.log")

        with open(file_name, "w") as f:
            f.write(f"{current_time}")

        print(f"{current_time} {file_name}")
        sleep(1)
