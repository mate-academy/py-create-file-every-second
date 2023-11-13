from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date_now = datetime.now()
        current_time = str(date_now.time()).split(":")
        hours = current_time[0]
        minutes = current_time[1]
        seconds = current_time[2].split(".")[0]

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(str(date_now))
        print(f"{date_now} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
