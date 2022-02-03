import datetime
import time


def create_a_file_every_sevond():
    while True:
        moment = datetime.datetime.now()
        name = f'app-{moment.hour}_{moment.minute}_{moment.second}.log'
        with open(f'{name}', 'w') as f:
            f.write(str(moment))
        print(str(moment), name)
        time.sleep(1)


if __name__ == '__main__':
    create_a_file_every_sevond()
