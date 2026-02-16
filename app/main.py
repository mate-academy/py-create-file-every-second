from datetime import datetime
from time import sleep


def main() -> None:
    while True:

        now = datetime.now().replace(microsecond=0)

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        time_stamp = str(now)

        with open(file_name, "w") as file:
            file.write(time_stamp)

        print(time_stamp, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
