from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"
        with open(file_name, "w") as file:
            file.write(date.strftime("%Y-%m-%d %H:%M:%S"))
        print(f'{date.strftime("%Y-%m-%d %H:%M:%S")} {file_name}')
        sleep(1)


if __name__ == "__main__":
    main()
