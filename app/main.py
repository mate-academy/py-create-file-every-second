from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = "app-" + time_now.strftime("%H_%M_%S") + ".log"
        with open(file_name, "w+") as f:
            f.write(time_now.strftime("%Y-%m-%d %H:%M:%S"))
            f.seek(0)
            print(f.read(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
