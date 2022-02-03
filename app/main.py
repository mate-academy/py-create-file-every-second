from time import sleep
from datetime import datetime


def loging():
    while True:
        with open(datetime.now().strftime("app-%H_%M_%S.log"), "w+") as file:
            file.write(str(datetime.now()))
        print(str(datetime.now()), datetime.now().strftime("app-%H_%M_%S.log"))
        sleep(1)


if __name__ == '__main__':
    loging()
