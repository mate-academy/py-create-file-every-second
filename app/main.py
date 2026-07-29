from datetime import datetime
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.time().hour
        minutes = current_time.time().minute
        seconds = current_time.time().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(current_time))
        print(f"{str(current_time)} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
