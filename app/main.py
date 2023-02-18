from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        value = datetime.now()
        data = str(value)

        with open(f"app-{value.hour}_{value.minute}_{value.second}.log",
                  "w") as file:
            file.write(data)

        print(f"{data} app-{value.hour}_{value.minute}_{value.second}.log")
        time.sleep(1)
