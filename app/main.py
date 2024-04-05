from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        formate_time = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as file:
            file.write(str(now))
            print(formate_time, " ", file_name)
            sleep(1)


if __name__ == "__main__":
    main()
