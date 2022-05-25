import time
from datetime import datetime


def create_file_every_second():
    while True:
        cur_time = datetime.now()
        file_name = f"app-{cur_time.hour}_{cur_time.minute}_" \
                    f"{cur_time.second}.log"
        file_content = str(cur_time)
        with open(file_name, "w") as f:
            f.write(file_content)
            print(file_content, file_name)
        time.sleep(1)


if __name__ == '__main__':
    create_file_every_second()
