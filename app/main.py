from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        with open(f'app-{current_date.strftime("%H_%M_%S")}.log', "w") as f:
            str_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
            f.write(str_date)
            print(str_date, f.name)
        sleep(1)


if __name__ == "__main__":
    main()
