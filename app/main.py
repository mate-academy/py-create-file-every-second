from datetime import datetime
from time import sleep


def file_creation():
    while True:
        timestamp = datetime.now()
        file_name = (
            f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"
        )

        with open(file_name, "w") as f:
            f.write(str(timestamp))

        print(str(timestamp), file_name)
        sleep(1)


if __name__ == '__main__':
    file_creation()
