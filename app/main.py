from datetime import datetime
from time import sleep


def w_file_every_second():
    for _ in range(3):
        now = datetime.now()
        filename = now.strftime("app-%H_%M_%S.log")
        with open(filename, "w") as f:
            f.write(f"{now}")
            sleep(1)
