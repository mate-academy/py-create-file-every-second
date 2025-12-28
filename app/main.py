from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        with open(date.strftime("app-%H_%M_%S.log"), "w") as f:
            f.write(str(date))
        with open(date.strftime("app-%H_%M_%S.log"), "r") as f:
            print(f.read() + " " + date.strftime("app-%H_%M_%S.log"))
        sleep(1)


print(str(datetime.now()))

if __name__ == "__main__":
    main()
