from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (f"app-{time_now.hour}"
                     f"_{time_now.minute}"
                     f"_{time_now.second}.log")
        with open(file_name, "w") as next_file:
            next_file.write(f"{time_now}")
        print(f"{time_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
