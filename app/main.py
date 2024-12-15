from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        data_now = datetime.now()
        file_name = (f"app-{data_now.hour}_"
                     f"{data_now.minute}_"
                     f"{data_now.second}.log")
        with open(file_name, "w") as f:
            f.write(f"{data_now}")
        print(f"{data_now} {file_name}")  # Debug output
        sleep(1)


if __name__ == "__main__":
    main()
