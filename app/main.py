from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        file = f"app-" \
               f"{datetime.now().hour}_" \
               f"{datetime.now().minute}_" \
               f"{datetime.now().second}.log"
        datetime_object = datetime.now()
        with open(file, "w") as f:
            f.write(f"{datetime_object}")
        print(f"{datetime_object} {file}")
        sleep(1)


if __name__ == '__main__':
    main()
