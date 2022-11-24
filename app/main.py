import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        time_for_filename = datetime.now().strftime("%H_%M_%S")
        new_file_name = f"app-{time_for_filename}.log"
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(f"{new_file_name}", "w+") as new_file:
            new_file.write(f"{current_datetime}")

        with open(new_file_name, "r") as reading_file:
            print(f"{reading_file.read()} {new_file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
