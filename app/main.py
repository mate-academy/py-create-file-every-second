from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        formatted_time = now.strftime("%H_%M_%S")
        file_name = f"app-{formatted_time}.log"
        with open(file_name, "w") as file:
            file.write(formatted_date)
            print(formatted_date, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
