from time import sleep
from datetime import datetime


def main():
    while True:
        sleep(1)
        with open(f"app-{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}.log", "w") as f:
            f.write(str(datetime.now()))
        print(datetime.now(), f.name)

if __name__ =='__main__':
    main()
