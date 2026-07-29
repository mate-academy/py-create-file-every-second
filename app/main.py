from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.strftime("%H")
        minutes = current_time.strftime("%M")
        seconds = current_time.strftime("%S")

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as name_file:
            name_file.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))

        print(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
