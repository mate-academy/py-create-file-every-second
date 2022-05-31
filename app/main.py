from datetime import datetime
from time import sleep


def w_file_every_second():
    while True:
        now = datetime.now()
        filename = now.strftime("app-%H_%M_%S.log")
        with open(filename, "w") as f:
            f.write(f"{now}")
            sleep(1)

        print(now, filename)
