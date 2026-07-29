from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        date_time = datetime.now()

        formatted_time = date_time.strftime("%H_%M_%S")
        formatted_date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")

        file_name = f"app-{formatted_time}.log"
        with open(file_name, "w") as file:
            file.write(formatted_date_time)

        print(formatted_date_time, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
