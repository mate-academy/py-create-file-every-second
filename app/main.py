from datetime import datetime
import time


def app():
    while True:
        file_name = datetime.now()
        file_name_time = f'app-{file_name.hour}_' \
                         f'{file_name.minute}_' \
                         f'{file_name.second}.log'
        with open(file_name_time, 'w') as file:
            file.writelines(str(file_name) + ' ' + file_name_time)
            print(file_name, file_name_time)
        time.sleep(1)


if __name__ == '__main__':
    app()
