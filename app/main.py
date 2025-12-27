from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        date_format = time_now.strftime("%Y-%m-%d %H:%M:%S")
        hours = time_now.hour
        minutes = time_now.minute
        seconds = time_now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as file:
            file.write(date_format)
        print(f"{date_format} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
