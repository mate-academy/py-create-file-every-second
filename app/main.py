from datetime import datetime
from time import sleep


def main():
    while True:
        with open(f"app-{datetime.now().hour}"
                  f"_{datetime.now().minute}"
                  f"_{datetime.now().second}.log",
                  "w") as f:
            f.write(str(datetime.now()))
            print(str(f"{datetime.now()} app-{datetime.now().hour}"
                      f"_{datetime.now().minute}"
                      f"_{datetime.now().second}.log"))
            sleep(1)


if __name__ == "__main__":
    main()
