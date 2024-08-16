from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}"
                     f"_{datetime.now().minute}"
                     f"_{datetime.now().second}.log")
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))
        print(f"{datetime.now()} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
