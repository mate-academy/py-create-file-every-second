from datetime import datetime
from time import sleep


def main():
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        date = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            f.write(date)
            print(date, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
