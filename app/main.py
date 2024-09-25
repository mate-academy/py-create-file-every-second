from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        current_date = datetime.now()
        file_name = f"app-{current_date.strftime("%H_%M_%S")}.log"

        with open(file_name, "w") as f:
            f.write(f"{current_date}")
            print(f"{current_date} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
