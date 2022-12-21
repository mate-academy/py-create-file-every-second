from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        new_file = f"app-{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}.log"
        with open(new_file, "a+") as f:
            f.write(f"{datetime.now()}")
            print(datetime.now(), new_file)
        sleep(1)


if __name__ == "__main__":
    main()
