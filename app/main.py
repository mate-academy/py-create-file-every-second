import datetime
import time


def create_a_file_every_second():
    while True:
        now = str(datetime.datetime.now())
        file_name = f"app-{now[11:13]}_{now[15:17]}_{now[18:20]}.log"

        with open(file_name, "w") as f:
            f.write(f"{datetime.datetime.now()}" + "\n")

        print(f"The file {file_name} created successfully")
        time.sleep(1)
