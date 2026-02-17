from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> str:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, mode="w", encoding="utf-8") as file:
            file.write(str(now))

        print(f"{str(now)[:19]} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
