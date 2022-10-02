from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"
        time_content = date.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(time_content)

        with open(file_name, "r") as file:
            print(file.read(), file_name)

        sleep(1)


if __name__ == "__main__":
    main()
