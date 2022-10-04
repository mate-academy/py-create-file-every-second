from datetime import datetime
from time import sleep


def main():
    while True:
        now = datetime.now()
        name = f'app-{now.hour}_{now.minute}_{now.second}.log'
        with open(name, "w") as new_file:
            new_file.write(str(datetime.now()))
        print(now, name)
        sleep(1)


if __name__ == "__main__":
    main()
