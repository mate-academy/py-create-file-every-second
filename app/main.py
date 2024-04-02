from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        file_name = (f"app-{timestamp.hour}"
                     f"_{timestamp.minute}_{timestamp.second}.log")
        with open(file_name, "w") as file:
            file.write(str(timestamp))
        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
