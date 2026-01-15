import time
from datetime import datetime


def create_file() -> None:
    current_time = datetime.now()
    filename = (f"app-{current_time.hour}"
                f"_{current_time.minute}"
                f"_{current_time.second}.log")
    file_content = f"{current_time}"

    with open(filename, "w") as f:
        f.write(file_content)
    print(f"{current_time} {filename}")


def read_and_print_file(filename: str) -> None:
    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            print(content)
    except FileNotFoundError:
        print(f"File{filename} not found")


def main() -> None:
    while True:
        create_file()
        time.sleep(1)


if __name__ == "__main__":
    main()
