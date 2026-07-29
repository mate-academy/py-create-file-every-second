from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # date = datetime(2022, 12, 31, 23, 59, 12)
    while True:
        # date = datetime(2022, 12, 31, 23, 59, 12)
        date = datetime.now()
        file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"
        with open(file_name, "w") as f:
            f.write(f"{datetime.now()}")
        print(f"{datetime.now()} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
