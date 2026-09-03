from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        name = "app-" + now.strftime("%H_%M_%S" + ".log",)
        with open(name, "w") as f:
            f.write(time_stamp)
        print(time_stamp, name)
        sleep(1)


if __name__ == "__main__":
    main()
