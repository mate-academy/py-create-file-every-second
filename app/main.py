from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (
            f"app-{current_time.hour}_{current_time.minute}_"
            f"{current_time.second}.log"
        )
        beautiful_date = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(beautiful_date)

        print(f"{beautiful_date} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
