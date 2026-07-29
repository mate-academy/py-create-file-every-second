from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as file:
            file.write(str(now))
        print(f"{now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
