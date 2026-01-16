from datetime import datetime
from time import sleep
from os import path


def main() -> None:
    current_folder = path.basename(path.abspath(path.dirname(__file__)))

    while True:
        ts = datetime.now()
        hours, minutes, seconds = ts.hour, ts.minute, ts.second

        file_name = f"{current_folder}-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as file:
            file.write(str(ts))

        print(f"{str(ts)} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
