import datetime
import time


def every_second_file():
    while True:
        date_now = datetime.datetime.now()
        full_date = f"app-{date_now.hour}" \
                    f"_{date_now.minute}" \
                    f"_{date_now.second}.log"

        with open(full_date, 'w') as file:
            file.write(str(date_now))

        print(str(date_now) + ' ' + full_date)
        time.sleep(1)


if __name__ == '__main__':
    every_second_file()
