from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f'app-{datetime.now().strftime("%H_%M_%S")}.log'

        with open(filename, "w") as file:
            file.write(current_date)

        print(current_date, filename)
        sleep(1.0)


if __name__ == "__main__":
    main()
