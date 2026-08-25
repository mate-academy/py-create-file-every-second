import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        name = (f"app-"
                f"{datetime.now().hour}_"
                f"{datetime.now().minute}_"
                f"{datetime.now().second}.log")
        with open(name, "a") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name)
        time.sleep(1)


if __name__ == "__main__":
    main()
