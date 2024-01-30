from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        name_file = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(name_file, "w") as file:
            file.write(f"{datetime.now()}")
        with open(name_file, "r") as file:
            print(f"{file.read()} {name_file}")
            time.sleep(1)


if __name__ == "__main__":
    main()
