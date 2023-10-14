from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_datetime = datetime.now()
        file_name = (f"app-{current_datetime.hour}_"
                     f"{current_datetime.minute}_"
                     f"{current_datetime.second}.log")

        with open(file_name, "w") as f:
            f.write(f"{current_datetime}")

        print(f"{current_datetime} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
