from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        time_marker = f"{now.strftime("%Y-%m-%d")} {now.strftime("%H:%M:%S")}"
        with open(file_name, "w") as file:
            file.write(f"{time_marker}")

        print(f"{time_marker} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
