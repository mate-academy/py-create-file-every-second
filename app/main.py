import datetime
import time


def create_file_every_second():
    while True:
        now = datetime.datetime.now()
        file_name = 'app-' + now.strftime("%H_%M_%S") + '.log'
        content = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        with open(file_name, "w") as f:
            f.write(content)
            print(content, file_name)
        time.sleep(1)


if __name__ == '__main__':
    create_file_every_second()
