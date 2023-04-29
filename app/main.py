from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        name = f'app-{datetime.now().strftime("%H_%M_%S")}.log'
        app = open(name, "w")
        app.write(str(datetime.now()))
        print(str(datetime.now()) + " " + name)
        sleep(1)


if __name__ == "__main__":
    main()
