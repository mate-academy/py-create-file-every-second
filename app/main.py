from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        name_file = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_"
                     f"{datetime.now().second}.log")
        with open(name_file, "w") as file:
            file.write(str(datetime.now()))
        with open(name_file, "r") as file:
            print(file.read(), file.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
