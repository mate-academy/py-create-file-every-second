import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date = datetime.now()

        file_name = f"app-{date.hour}_{date.minute}_{date.second}.log"

        with open(file_name, "w") as f:
            f.write(str(date))
            print(date, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
