from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        with open(
                f"app-{date.hour}_{date.minute}_{date.second}.log",
                "w+"
        ) as file:
            file.write(str(date))
            file.seek(0)
            print(file.read(), file.name)
            sleep(1)


if __name__ == "__main__":
    main()
