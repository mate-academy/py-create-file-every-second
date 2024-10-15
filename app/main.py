from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        with open(
            "app-" + datetime.now().strftime("%H_%M_%S") + ".log", "w"
        ) as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f.name)
        sleep(1)


if __name__ == "__main__":
    main()
