import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_without_date = current_time.split(" ")
        file_name = f"app-{time_without_date[1].replace(':', '_')}.log"
        with open(file_name, "a") as file:
            file.write(current_time)
        print(f"{current_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
