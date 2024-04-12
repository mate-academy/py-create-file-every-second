from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def create_log_file() -> None:
    current_time = datetime.now()
    file_name = "app-{}_{}_{}.log".format(
        current_time.hour, current_time.minute, current_time.second
    )
    file_content = str(current_time)

    with open(file_name, "w") as file:
        file.write(file_content)

    print(f"{current_time} {file_name}")


def main() -> None:
    while True:
        create_log_file()
        sleep(1)


if __name__ == "__main__":
    main()
