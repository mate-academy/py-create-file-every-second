from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        time = datetime.now()
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(file_name, "w") as file:
            file.write(str(time))
            print(f"{time} app-{time.hour}_{time.minute}_{time.second}.log")
            sleep(1)


if __name__ == "__main__":
    main()
