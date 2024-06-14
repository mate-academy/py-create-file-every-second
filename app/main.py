import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_{current_time.second}.log")
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(file_content)

        print(f"{file_content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
