from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        time_formated = time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"

        with open(file_name, "w+") as file:
            sleep(1)
            file.write(time_formated)
            file.seek(0)
            print(file.read(), file_name)


if __name__ == "__main__":
    main()
