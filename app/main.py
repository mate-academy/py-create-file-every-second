from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = (f"app-{now.hour}"
                     f"_{now.minute}"
                     f"_{now.second}.log")
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        print(timestamp, file_name)

        with open(file_name, "x") as file:
            file.write(f"{timestamp}")

        sleep(1)


if __name__ == "__main__":
    main()
