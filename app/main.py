from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name = now.strftime("app-%H_%M_%S.log")
        with open(name, "w") as file:
            file.write(str(now))
        print(f"{now} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
