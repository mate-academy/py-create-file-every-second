from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        name_of_file = \
            (f"app-{datetime.now().strftime('%H')}"
             f"_{datetime.now().strftime('%M')}"
             f"_{datetime.now().strftime('%S')}.log")
        with open(name_of_file, "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name_of_file)
        sleep(1)


if __name__ == "__main__":
    main()
