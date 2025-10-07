from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = "app-" + datetime.now().strftime("%H_%M_%S") + ".log"
        with open(file_name, "w") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
