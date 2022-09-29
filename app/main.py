from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def repeat(f):
    def inner():
        while True:
            f()
            sleep(1)

    return inner


@repeat
def main():
    date = datetime.now()
    with open(f"app-{date.hour}_{date.minute}_{date.second}.log", "x") as file:
        file.write(f"{date}")
        print(f"{date} {file.name}")


if __name__ == "__main__":
    main()
