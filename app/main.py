from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(str(current_time))
        print(current_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
