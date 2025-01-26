import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def print_file(date: str, filename: str) -> None:
    with open(f"{filename}", "w") as file:
        file.write(date)
    file.close()
    print(date, filename)


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.strftime('%H_%M_%S')}.log")
        print_file(
            filename=file_name,
            date=f"{current_time}"
        )
        time.sleep(1)


if __name__ == "__main__":
    main()
