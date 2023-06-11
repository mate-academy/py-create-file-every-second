from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        current_time = current_date.strftime("%H_%M_%S")
        file_name = f"app-{current_time}.log"

        with open(file_name, "w") as file:
            file.write(str(current_date))
            print(current_date, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
