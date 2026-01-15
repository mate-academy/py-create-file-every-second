from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time = datetime.now()
        filename = f"app-{date_time.strftime('%H_%M_%S')}.log"
        with open(filename, "w") as fl:
            fl.write(str(date_time))
        print(date_time, filename)
        sleep(1)


if __name__ == "__main__":
    main()
