from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_"
                     f"{datetime.now().second}.log")
        content = str(datetime.now())
        with open(file_name, "w") as log:
            log.write(content)
            print(content, file_name)
            sleep(1)


if __name__ == "__main__":
    main()
