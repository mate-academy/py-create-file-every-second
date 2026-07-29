from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        current_filename = (f"app-{current_datetime.hour}_"
                            f"{current_datetime.minute}_"
                            f"{current_datetime.second}.log")
        with open(current_filename, "w") as f:
            f.write(f"{current_datetime}")
            print(current_datetime, current_filename)
            sleep(1)


if __name__ == "__main__":
    main()
