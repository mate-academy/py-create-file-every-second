import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name = (f"app-{datetime.now().hour}_{datetime.now().minute}"
                f"_{datetime.now().second}.log")
        with open(name, "w") as file:
            file.write(f"{datetime.now()}")
            print(f"{datetime.now()} {name}")
            file.close()
            time.sleep(1)


if __name__ == "__main__":
    main()
