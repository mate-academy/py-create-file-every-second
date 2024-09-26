from datetime import datetime
from time import sleep


def main():
    while True:
        name = datetime.now().strftime("app-%H_%M_%S.log")
        content = str(datetime.now())
        with open(name, "w+") as f:
            f.write(content)
        with open(name, 'r') as f:
            print(f"{f.read()} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
