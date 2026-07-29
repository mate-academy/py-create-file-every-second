from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now_time = datetime.now()
        file_name_format = (f"app-{now_time.hour}"
                            f"_{now_time.minute}"
                            f"_{now_time.second}.log")
        file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name_format, "w") as file:
            file.write(file_content)
        print(file_content, file_name_format)
        sleep(1)


if __name__ == "__main__":
    main()
