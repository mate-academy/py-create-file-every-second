from datetime import datetime
from time import sleep


def file_every_second():
    while True:
        time = datetime.now()
        name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(name, "w") as f:
            f.write(str(time))
        print(str(time) + " " + name)
        sleep(1)


if __name__ == '__main__':
    file_every_second()
