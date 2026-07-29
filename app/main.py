from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def create_file() -> str:
    current_date = datetime.now()
    hours = current_date.hour
    minutes = current_date.minute
    seconds = current_date.second
    file_name = f"app-{hours}_{minutes}_{seconds}.log"
    content = str(current_date)
    with open(file_name, "w") as f:
        f.write(content)
    print(f"{current_date} {file_name}")


def main() -> None:
    while True:
        create_file()
        sleep(1)


if __name__ == "__main__":
    main()
