from datetime import datetime
from time import sleep


def create_file(file_name: str, content: str) -> None:
    with open(file_name, "a") as document:
        document.write(content)


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_{current_time.minute}"
                     f"_{current_time.second}.log")

        create_file(file_name, str(current_time))
        print(current_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
