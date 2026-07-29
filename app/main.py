from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_output = open(f"app-"
                           f"{datetime.now().hour}_"
                           f"{datetime.now().minute}_"
                           f"{datetime.now().second}"
                           f".log", "w")
        file_output.write(f"{datetime.now()}")
        print(datetime.now(), file_output.name)
        sleep(1)


if __name__ == "__main__":
    main()
