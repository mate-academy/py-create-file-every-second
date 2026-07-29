from datetime import datetime
from time import sleep


def main():
    while True:
        n = datetime.now()
        with open(
                f"app-{n.hour}_{n.minute}_{n.second}.log",
                "w"
        ) as f:
            f.write(n.__str__())
            print((n.__str__() + f" app-{n.hour}_{n.minute}_{n.second}.log"))
            sleep(1)


if __name__ == "__main__":
    main()
