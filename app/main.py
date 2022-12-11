from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = "app-" + now.strftime("%H_%M_%S") + ".log"
        file = open(file_name, "w")
        file.write(str(now))
        print(now, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
