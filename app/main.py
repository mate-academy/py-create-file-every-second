from datetime import datetime
from time import sleep


def main():
    while True:
        with open(f"app-{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}.log", "w+") as f:
            text = f"{datetime.now()}"
            f.write(text)
            print(text, f.name)
        sleep(1)


if __name__ == "__main__":
    main()
