from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (f"app-{current_date.hour}_"
                     f"{current_date.minute}_"
                     f"{current_date.second}.log")

        with open(file_name, "w") as f:
            f.write(timestamp)

        print(timestamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
