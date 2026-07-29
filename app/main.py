from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name = str(datetime.now().strftime("%H_%M_%S"))
        content = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        with open("app-" + name + ".log", "a") as file:
            file.write(content)

        print(content + " " + "app-" + name + ".log")

        sleep(1)


if __name__ == "__main__":
    main()
