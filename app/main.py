from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now_date = datetime.now()
        file_content = f"{now_date:%Y-%m-%d %H:%M:%S}"
        file_name = (f"app-{now_date.hour}_"
                     f"{now_date.minute}_"
                     f"{now_date.second}.log")
        print(f"{file_content} {file_name}")
        with open(file_name, "w") as file:
            file.write(f"{file_content}")
        sleep(1)


if __name__ == "__main__":
    main()
