from datetime import datetime
import time


def app():
    while True:
        file_name = datetime.now()
        with open(
                f'app-{file_name.hour}_{file_name.minute}'
                f'_{file_name.second}.log', 'w'
        ) as file:
            file.writelines(
                str(file_name) + f' app-{file_name.hour}'
                                 f'_{file_name.minute}_{file_name.second}.log'
            )
            print(file_name, f'app-{file_name.hour}'
                             f'_{file_name.minute}_{file_name.second}.log')
        time.sleep(1)


if __name__ == '__main__':
    app()
