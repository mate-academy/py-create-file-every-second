import datetime
import time


def create_log_file() -> str:
    current_datetime = datetime.now()
    filename = f"app-{current_datetime.hour:02d}_" \
               f"{current_datetime.minute:02d}_" \
               f"{current_datetime.second:02d}.log"
    file_content = str(current_datetime)

    with open(filename, "w") as file:
        file.write(file_content)

    print(f"{current_datetime} {filename}")


def main() -> int:
    while True:
        create_log_file()
        time.sleep(1)


if __name__ == "__main__":
    main()
