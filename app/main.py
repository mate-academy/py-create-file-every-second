from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep
from typing import NoReturn


def generate_log_files() -> NoReturn:
    while True:
        now = datetime.now()

        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(filename, "w") as f:
            f.write(str(now))

        print(f"{now} {filename}")

        sleep(1)


def main() -> NoReturn:
    generate_log_files()


if __name__ == "__main__":
    main()
