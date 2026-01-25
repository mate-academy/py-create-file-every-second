from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        time_now = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.strftime('%H_%M_%S')}.log"
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(f"{time_now}")
            print(f"{time_now} {file_name}")
            sleep(1)


if __name__ == "__main__":
    main()
