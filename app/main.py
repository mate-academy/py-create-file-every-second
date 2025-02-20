from datetime import datetime
from time import sleep


def main() -> None:
    def create_log_files() -> None:
        while True:
            timestamp = datetime.now()
            file_name = (f"app-{timestamp.hour}_{timestamp.minute}"
                         f"_{timestamp.second}.log")
            file_content = timestamp.strftime("%Y-%m-%d %H:%M:%S")

            with open(file_name, "w", encoding="utf-8") as file:
                file.write(file_content)

            print(f"{file_content} {file_name}")
            sleep(1)

    create_log_files()


if __name__ == "__main__":
    main()
