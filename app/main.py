from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        only_time = date.strftime("%H_%M_%S")
        name_of_file = f"app-{only_time}.log"
        with open(name_of_file, "w") as f:
            f.write(date.strftime("%Y-%m-%d %H:%M:%S"))
        sleep(1)
        with open(name_of_file, "r") as f:
            print(f.read(), name_of_file)


if __name__ == "__main__":
    main()
