from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        formated_date = date.strftime("%H_%M_%S")
        filename = "app-" + formated_date + ".log"
        with open(filename, mode="w") as file:
            content = date.strftime("%Y-%m-%d %H:%M:%S")
            file.write(content)
        print(content, filename)
        sleep(1)


if __name__ == "__main__":
    main()
