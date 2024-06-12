from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        filename = now.strftime("app-%H_%M_%S.log")
        with open(filename, "w") as f:
            f.write(f"{now}")
            sleep(1)

        print(now, filename)


if __name__ == "__main__":
    main()
