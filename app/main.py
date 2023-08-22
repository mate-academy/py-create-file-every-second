from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_"
                     f"{datetime.now().second}.log")
        with open(file_name, "w") as f:
            f.write(f"{datetime.now()}")
        print(f"{datetime.now()} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
