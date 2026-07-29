from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        with open(filename, "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print(f"{datetime.now()} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
