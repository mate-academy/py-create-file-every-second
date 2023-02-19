from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time = f"app-{datetime.now().hour}_" \
                    f"{datetime.now().minute}_" \
                    f"{datetime.now().second}"
        with open(f"{date_time}.log", "w+") as new_file:
            new_file.write(f"{datetime.now()}")
            print(datetime.now(), new_file.name)
            sleep(1)


if __name__ == "__main__":
    main()
