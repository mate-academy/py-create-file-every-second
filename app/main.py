from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        name_of_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        name_of_file = current_time.strftime("app-%H_%M_%S.log")
        with open(name_of_file, "w") as f:
            f.write(name_of_current_time)
            print(name_of_current_time, name_of_file)
        sleep(1)


if __name__ == "__main__":
    main()
