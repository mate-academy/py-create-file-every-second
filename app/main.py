import time
from datetime import datetime


def create_file_every_second():
    while True:
        file_name = f"app-{datetime.now().hour}_{datetime.now().minute}_" \
                    f"{datetime.now().second}.log"
        file_content = str(datetime.now())
        with open(file_name, "w") as f:
            f.write(file_content)
            print(file_content, file_name)
        time.sleep(1)


if __name__ == '__main__':
    create_file_every_second()
