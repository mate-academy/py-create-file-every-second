from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        stamp = f"{year}-{month}-{day} {hour}:{minute}:{second}"
        with open(file_name, "w") as f:
            f.write(stamp)
        print(f"{stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
