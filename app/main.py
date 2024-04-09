from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        time_now = (datetime.now().hour,
                    datetime.now().minute,
                    datetime.now().second)
        file_name = "app-{}_{}_{}.log".format(*time_now)
        with open(file_name, "a") as file:
            file.write(str(datetime.now()))
        print(datetime.now(), file_name)

        sleep(1)


if __name__ == "__main__":
    main()
