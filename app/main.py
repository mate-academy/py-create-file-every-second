from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        formated = now.strftime("app-%H_%M_%S.log")
        line = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(formated, "w") as obj_file:
            obj_file.write(line)
        print(line, formated)
        sleep(1)


if __name__ == "__main__":
    main()
