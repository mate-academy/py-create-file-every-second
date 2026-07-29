from datetime import datetime
from time import sleep


def main() -> print:
    while True:
        now = datetime.now()
        time = now.strftime("app-%H_%M_%S.log")
        with open(time, "w") as new_file:
            new_file.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        with open(time, "r") as new_file:
            print(new_file.read(), time)

        sleep(1)


if __name__ == "__main__":
    main()
