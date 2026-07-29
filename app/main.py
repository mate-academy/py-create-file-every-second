from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        date = datetime.now()
        file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"

        print(date.strftime("%Y-%m-%d %H:%M:%S"), end=" ")
        print(file_name)

        with open(file_name, "w") as file:
            file.write(date.strftime("%Y-%m-%d %H:%M:%S"))

        sleep(1)


if __name__ == "__main__":
    main()
