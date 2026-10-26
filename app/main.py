from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        date_to_write = now.strftime("%Y-%m-%d %H:%M:%S")
        fl = open(file_name, "w")
        fl.write(date_to_write)
        fl.close()
        print(date_to_write, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
