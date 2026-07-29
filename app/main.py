from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        right_now = datetime.now()
        file_name = (f"app"
                     f"-{right_now.hour}"
                     f"_{right_now.minute}"
                     f"_{right_now.second}.log")
        timestamp = right_now.strftime("%Y-%m-%d %H:%M:%S")
        sleep(1)
        with open(file_name, "w") as file:
            file.write(timestamp)
        print(timestamp, file_name)


if __name__ == "__main__":
    main()
