from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        hour = time.hour
        minute = time.minute
        second = time.second
        now = datetime.now()
        full_date = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(file_name, "w") as f:
            f.write(full_date)
            print(f"{full_date} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
