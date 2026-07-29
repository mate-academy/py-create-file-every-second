from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(f"{file_name}", "w") as file:
            file.write(str(time))
            sleep(1)
        print(time, file_name)


if __name__ == "__main__":
    main()
