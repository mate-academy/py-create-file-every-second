import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    # write your code here
    while True:
        name = (f"app-{datetime.now().hour}_{datetime.now().minute}"
                f"_{datetime.now().second}.log")
        new_file = open(name, "w")
        print(f"{datetime.now()} {name}")
        new_file.write(datetime.now().__str__())
        new_file.close()
        time.sleep(1)


if __name__ == "__main__":
    main()
