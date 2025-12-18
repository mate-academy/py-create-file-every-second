from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        name = datetime.now()
        log = name.strftime("app-%H_%M_%S.log")
        with open(log, "w") as f:
            time = name.strftime("%Y-%m-%d %H:%M:%S")
            f.write(str(time))
        print(time + " " + log)
        sleep(1)


if __name__ == "__main__":
    main()
