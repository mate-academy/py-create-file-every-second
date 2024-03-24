from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        curr_date = datetime.now()
        filename = (f"app-{curr_date.hour}_"
                    f"{curr_date.minute}_{curr_date.second}.log")
        with open(filename, "w+") as file:
            file.write(str(curr_date))
        print(f"{str(curr_date)} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
