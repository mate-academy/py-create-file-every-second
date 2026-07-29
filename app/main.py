from datetime import datetime
from time import sleep


def main():
    while True:
        file_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as f:
            f.write(f"{datetime.now()}")
        with open(file_name, "r") as f:
            print(f"{f.read()} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
