from time import sleep
from datetime import datetime


def main():
    while True:
        date_now = datetime.now()
        timestamp = date_now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = \
            f"app-{date_now.hour}_{date_now.minute}_{date_now.second}.log"

        with open(file_name, "w") as f:
            f.write(timestamp)
        print(timestamp, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
