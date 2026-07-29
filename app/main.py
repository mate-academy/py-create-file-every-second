from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        name_now = datetime.now().strftime("app-%H_%M_%S.log")
        content = str(datetime.now())
        with open(name_now, "w+") as f:
            f.write(content)
        with open(name_now, 'r') as f:
            print(f"{f.read()} {name_now}")
        sleep(1)


if __name__ == "__main__":
    main()
