from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()  # Запам'ятали час один раз
        date_now = now.strftime("%Y-%m-%d %H:%M:%S")
        log_file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with (open(log_file_name, "w") as f):
            f.write(date_now)
        print(date_now, log_file_name)
        sleep(1)


if __name__ == "__main__":
    main()
