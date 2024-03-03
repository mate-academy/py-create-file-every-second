import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-"
                     f"{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        with open(file_name, "w") as file:
            file.write(str(current_time))
        print(f"{current_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
