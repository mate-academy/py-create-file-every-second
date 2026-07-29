from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        now_str = str(now)[:19]
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as file:
            file.write(now_str)
        print(now_str, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
