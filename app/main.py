from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name = "app-" + str(now.strftime("%H_%M_%S")) + ".log"
        with open(name, "a") as file:
            file.write(str(now))
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " " + name)
        sleep(1)


if __name__ == "__main__":
    main()
