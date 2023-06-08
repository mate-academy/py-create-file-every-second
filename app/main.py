from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
