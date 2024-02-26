import time
from datetime import datetime


def main() -> None:
    while True:
        time_is = datetime.now()
        time_string = time_is.strftime("%H_%M_%S")
        file_name = f"app-{time_string}.log"
        with open(file_name, "w") as file:
            date_string = str(time_is)
            file.write(date_string)
            print(date_string, file.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
