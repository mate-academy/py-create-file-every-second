from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        filename = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(filename, "w") as file:
            file.write(f"{time}")
            print(f"{time} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
