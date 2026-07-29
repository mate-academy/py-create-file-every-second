from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f""
                     f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(file_content)
            print(f"{file_content} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
