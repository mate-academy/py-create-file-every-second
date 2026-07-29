from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(name, "w") as file:
            file.write(str(now))
            print(str(now) + " " + name)
            sleep(1)


if __name__ == "__main__":
    main()
