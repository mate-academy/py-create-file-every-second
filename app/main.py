from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        ct = datetime.now()
        filename = f"app-{ct.hour}_{ct.minute}_{ct.second}.log"
        with open(filename, "a") as file:
            file.write(f"{ct}")
        print(f"{ct} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
