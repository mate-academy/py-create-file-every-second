from datetime import datetime  # DO NOT CHANGE THIS IMPORT

from time import sleep


def main() -> None:
    while True:
        date_full = datetime.now()
        date_for_name = date_full.strftime("%H_%M_%S")
        file_name = f"app-{date_for_name}.log"
        with open(file_name, "w") as f:
            f.write(str(date_full))
            print(date_full, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
