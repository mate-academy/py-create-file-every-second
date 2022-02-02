from datetime import datetime
from time import sleep


def files_generator():
    while True:
        t = datetime.now()
        file_name = f"app-{t.hour}_{t.minute}_{t.second}.log"
        print(str(t), file_name)
        sleep(1)
        with open(file_name, "a+") as f:
            f.write(str(t))


if __name__ == "__main__":
    files_generator()
