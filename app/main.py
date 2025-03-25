from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        date_today = f"{now.hour}_{now.minute}_{now.second}"
        name_of_file = f"app-{date_today}.log"

        with open(name_of_file, "a") as file:
            file.write(timestamp)

        sleep(1)
        print(f"{timestamp} {name_of_file}")


if __name__ == "__main__":
    main()
