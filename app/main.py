from time import sleep
from datetime import datetime


def create_log_every_second():

    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.hour}" \
                    f"_{current_time.minute}" \
                    f"_{current_time.second}.log"
        with open(file_name, "w") as f:
            f.write(str(current_time))
            print(current_time, file_name)
        sleep(1)


if __name__ == '__main__':
    create_log_every_second()
