from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(name, "w") as file:
            now = str(datetime.now())
            file.write(now)
            sleep(1)
            print(now, name)


if __name__ == "__main__":
    main()
