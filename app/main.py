from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as log:
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                  + " "
                  + file_name)
            log.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sleep(1)


if __name__ == "__main__":
    main()
