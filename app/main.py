from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        file_line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(f"{file_line}")

        print(f"{file_line} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
