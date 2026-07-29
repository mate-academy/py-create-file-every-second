from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = ("app-" + str(datetime.now().hour)
                    + "_" + str(datetime.now().minute)
                    + "_" + str(datetime.now().second)
                    + ".log")
        with open(filename, "a") as f:
            f.write(str(datetime.now()))
        print(f"{datetime.now()} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
