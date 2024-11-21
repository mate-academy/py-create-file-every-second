from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        hour = date.strftime("%H")
        minute = date.strftime("%M")
        second = date.strftime("%S")
        stamp = date.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{hour}_{minute}_{second}.log"

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(stamp)

        print(f"{stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
