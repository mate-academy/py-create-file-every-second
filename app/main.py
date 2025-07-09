from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w+") as f:
            f.write(f"{now}")
            print(f.read())
            sleep(1)


if __name__ == "__main__":
    main()
