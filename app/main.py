from datetime import datetime
from time import sleep


def file_creator():
    while True:
        time_now = datetime.now()
        file_name = f"app-{time_now.hour}"\
                    f"_{time_now.minute}"\
                    f"_{time_now.second}.log"
        with open(file_name, "w") as file:
            file.write(str(time_now))
        print(str(time_now) + ' ' + file_name)
        sleep(1)


file_creator()
