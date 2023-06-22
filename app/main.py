from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}_{datetime.now().minute}_"
                  f"{datetime.now().second}.log", "w") as f:
            f.write(str(datetime.now()))
        print(str(datetime.now()) + f" app-{datetime.now().hour}_"
                                    f"{datetime.now().minute}_"
                                    f"{datetime.now().second}.log")
        sleep(1)


if __name__ == "__main__":
    main()
