import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_and_date = datetime.now()
        file_name = (f"app-"
                     f"{time_and_date.hour}_{time_and_date.minute}"
                     f"_{time_and_date.second}"
                     + ".log")
        print(f"{time_and_date}" + " " + f"{file_name}")
        time.sleep(1)
        with open(file_name, "w") as f:
            f.write(f"{time_and_date}")


if __name__ == "__main__":
    main()
