from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep

DELAY = 1


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "a") as f:
            f.write(str(now))

        print(now, file_name)
        sleep(DELAY)


if __name__ == "__main__":
    main()
