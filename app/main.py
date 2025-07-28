from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        current_timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{current_date.strftime("%H_%M_%S")}.log"

        with open(file_name, "a") as file:
            file.write(current_timestamp)

        print(f"{current_timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
