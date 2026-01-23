from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-"
                     f"{datetime.now().hour}"
                     f"_{datetime.now().minute}"
                     f"_{datetime.now().second}.log")

        current_time = f"{datetime.now()}"

        with open(file_name, "w") as file:
            file.write(str(current_time))

        print(f"{current_time} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
