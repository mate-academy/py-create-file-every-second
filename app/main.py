from datetime import datetime
from time import sleep


def main():
    while True:
        try:
            filename = datetime.now().strftime("app-%H_%M_%S") + ".log"
            with open(filename, "w") as file:
                file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
