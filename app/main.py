from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        name=f"app-{now.strftime('%H_%M_%S')}"
        with open(f"{name}.log", "a") as log:
            log.write(f"{now}")
        print(f"{now} {name}.log")
        sleep(1)


if __name__ == "__main__":
    main()
