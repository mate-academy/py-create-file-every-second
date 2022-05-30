from time import sleep
from datetime import datetime


def main():
    while True:
        sleep(1)
        ct = datetime.now()
        name = f"app-{ct.hour}_{ct.minute}_{ct.second}.log"
        with open(name, "w") as f:
            f.write(str(datetime.now()))
        print(datetime.now(), f.name)


if __name__ == '__main__':
    main()
