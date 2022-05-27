from time import sleep
from datetime import datetime


def loging():
    while True:
        time_now = datetime.now()
        with open(time_now.strftime("app-%H_%M_%S.log"), "w+") as file:
            file.write(str(time_now))
        print(time_now, datetime.now().strftime("app-%H_%M_%S.log"))
        sleep(1)


if __name__ == '__main__':
    loging()
