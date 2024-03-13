from datetime import datetime
import time
from typing import NoReturn


def create_file() -> None:
    now = datetime.now()
    filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
    with open(filename, "w") as file:
        file.write(str(now))

    print(f"{now} {filename}")


def main() -> NoReturn:
    """Main function to continuously create files."""
    while True:
        create_file()
        time.sleep(1)


if __name__ == "__main__":
    main()
