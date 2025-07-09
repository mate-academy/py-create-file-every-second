from datetime import datetime
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        formated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(formated_time)

        print(f"{current_time} {file_name}")

        time.sleep(1)

if __name__ == "__main__":
    main()
#2020-01-01 14:10:09 app-14_10_9.log