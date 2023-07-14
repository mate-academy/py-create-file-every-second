from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        file_name = f"app-{date:%H_%M_%S}.log"
        with open(file_name, "w") as file:
            file.write(str(date))
        print(str(date), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
