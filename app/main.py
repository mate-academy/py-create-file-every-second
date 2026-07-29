from datetime import datetime
from time import sleep


def main():
    while True:
        file_name = f"app-{datetime.now().hour}" \
                    f"_{datetime.now().minute}_{datetime.now().second}.log"
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))
            print(f"{datetime.now()} {file_name}")
        sleep(1)
