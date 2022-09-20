from datetime import datetime
from time import sleep


def main():
    while True:
        current_time = datetime.now()
        with open(
                f'app-{current_time.hour}_{str(current_time.minute)}_'
                f'{str(current_time.second)}.log', 'w'
        ) as log:
            log.write(str(current_time))

            print(current_time, log.name)

        sleep(1)


if __name__ == "__main__":
    main()
