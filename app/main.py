from datetime import datetime
from time import sleep


def file_creating():
    while True:
        file_name = f"app-{datetime.today().strftime('%H_%M_%-S')}.log"
        timestamp = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
        with open(file_name, "w") as file:
            file.writelines(timestamp)
            print(timestamp, file_name)
        sleep(1)


if __name__ == "__main__":
    file_creating()
