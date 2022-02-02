from time import sleep
from datetime import datetime


def start_infinite_file_creation():
    while True:
        cur_time = datetime.now()
        with open(file=f"app-{cur_time.hour}_{cur_time.minute}_{cur_time.second}.log", mode='w') as fout:
            fout.write(str(cur_time))
            print(cur_time, fout.name)
        sleep(1)


if __name__ == '__main__':
    start_infinite_file_creation()
