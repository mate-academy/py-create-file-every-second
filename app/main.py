from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        with open(filename, "w") as f:
            f.write(f"{datetime.now()}")
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", filename)
        sleep(1)


if __name__ == "__main__":
    main()
