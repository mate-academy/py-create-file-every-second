from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        time = datetime.now()
        file_name = time.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as f:
            print(str(time) + " " + file_name)
            f.write(str(time))
        sleep(1)


if __name__ == "__main__":
    main()
