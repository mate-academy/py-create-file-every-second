import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name = (f"app-{datetime.now().hour}_{datetime.now().minute}"
                f"_{datetime.now().second}.log")
        print(str(datetime.now()) + " " + name)
        with open(name, "w") as f:
            f.write(str(datetime.now()))
        time.sleep(1)


if __name__ == "__main__":
    main()
