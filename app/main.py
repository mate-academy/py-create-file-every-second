from datetime import datetime

from time import sleep

from typing import Any


def main() -> Any:
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        name = f"app-{hour}_{minute}_{second}.log"
        with open(name, "w") as file1:
            new_line = f"{now}"
            file1.write(new_line)
        print(f"{now} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
