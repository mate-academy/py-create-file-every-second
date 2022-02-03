import datetime
import time


def create_a_file_every_second():
    while True:
        now = time.strftime("%R:%S").split(":")
        file_name = f"app-{now[0]}_{now[1]}_{now[2]}.log"

        with open(file_name, "w") as f:
            f.write(f"{datetime.datetime.now()}")

        print(f"{datetime.datetime.now()} {file_name}")
        time.sleep(1)
