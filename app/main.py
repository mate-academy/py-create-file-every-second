from datetime import datetime
import time


def create_file() -> None:
    current_time = datetime.now()
    file_name = "app-{}_{:02d}_{:02d}.log".format(
        current_time.hour, current_time.minute, current_time.second
    )
    file_content = str(current_time)

    with open(file_name, "w") as file:
        file.write(file_content)

    print(f"{current_time} {file_name}")


def main() -> None:
    while True:
        create_file()
        time.sleep(1)


if __name__ == "__main__":
    main()
