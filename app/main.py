from datetime import datetime
from time import sleep


def main():
    while True:
        now = datetime.now()
        current_time = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(current_time, "w") as file:
            file.write(str(now))
        with open(current_time, "r") as file:
            print(file.read() + " " + current_time)

        sleep(1)


if __name__ == "__main__":
    main()
