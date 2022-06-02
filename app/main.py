from time import sleep
from datetime import datetime


def main():
    while True:
        sleep(1)
        current_time = datetime.now()
        name = f"app-{current_time.hour}_{current_time.minute}_{current_time.second}.log"
        with open(name, "w") as f:
            f.write(str(current_time))
        print(current_time, f.name)


if __name__ == '__main__':
    main()
