from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = str(datetime.now())
        name = "app-" + now.split()[1].split(".")[0].replace(":", "_") + ".log"
        with open(name, "w") as file:
            file.write(now)
        print(now, name)
        sleep(1)


if __name__ == "__main__":
    main()
