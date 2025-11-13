from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        with open(f"app-{datetime.now().strftime('%H_%M_%S')}"
                  f".log", "w", encoding="utf-8") as file:
            date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(date_now)
            print(f"{date_now} {file.name}")
            sleep(1)


if __name__ == "__main__":
    main()
