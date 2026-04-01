from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(now.strftime("app-%H_%M_%S.log"), "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} "
                  f"{now.strftime('app-%H_%M_%S.log')}")
            sleep(1)


if __name__ == "__main__":
    main()
