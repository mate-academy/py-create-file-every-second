from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        with open(f'app-{datetime.now().strftime("%H_%M_%S")}.log', "w") as f:
            f.write(f"{datetime.now()}")
            print(f"{datetime.now()} "
                  f"app-{datetime.now().strftime("%H_%M_%S")}.log")
            sleep(1)


if __name__ == "__main__":
    main()
