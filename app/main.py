from datetime import datetime
from time import sleep


def file_creator():
    while True:
        with open(f"app-{datetime.now().hour}"
                  f"_{datetime.now().minute}"
                  f"_{datetime.now().second}.log", "w") as file:

            file.write(str(datetime.now()))
        sleep(1)


file_creator()
