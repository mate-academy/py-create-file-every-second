from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current = datetime.now()
        file_name = f"app-{current.hour}_{current.minute}_{current.second}.log"
        with open(file_name, "w") as file:
            file.write(str(current))
            print(str(current), file_name)
        sleep(1)
