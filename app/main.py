from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        file_name = datetime.now().strftime("app-%H_%M_%S.log")
        line = str(datetime.now())
        with open(file_name, "w") as f:
            f.write(line)
        print(line, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
