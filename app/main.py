from datetime import datetime


import time


def main() -> None:
    while True:
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        log_file_name = "app-" + now.strftime("%H_%M_%S") + ".log"

        try:
            with open(log_file_name, "w") as file:
                file.write(date_time)
        except Exception as e:
            print(e)
        else:
            print(f"{date_time} {log_file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
