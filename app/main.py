from time import sleep
from datetime import datetime


def start_infinite_file_creation():
    while True:
        cur_time = datetime.now()
        file_name = f"app-" \
                    f"{cur_time.hour}_" \
                    f"{cur_time.minute}_" \
                    f"{cur_time.second}.log"
        with open(file=file_name, mode='w') as fout:
            fout.write(str(cur_time))
            print(cur_time, fout.name)
        sleep(1)


if __name__ == '__main__':
    start_infinite_file_creation()
