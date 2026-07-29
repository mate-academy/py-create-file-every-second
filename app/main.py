from datetime import datetime
from time import sleep


def main():
    while True:

        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as f:
            f.write(str(now))
        sleep(1)
        print(f"{now} {file_name}")


if __name__ == "__main__":
    main()
