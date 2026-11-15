from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        today = datetime.now()
        formated_date = today.strftime("%H_%M_%S")
        formate_date = today.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{formated_date}.log"
        with open(file_name, "w") as file:
            file.write(formate_date)
        print(formate_date, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
