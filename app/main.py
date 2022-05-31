import datetime
import time


def main():
    while True:
        date_now = datetime.datetime.now()
        time_info = f"{datetime.datetime.now().hour}_" \
                    f"{datetime.datetime.now().minute}_" \
                    f"{datetime.datetime.now().second}"

        with open(f"app-{time_info}.log", "w") as log_file:
            log_file.write(f"{date_now}")

        print(f"app-{time_info}.log")
        print(f"{date_now}")
        time.sleep(1)


if __name__ == "__main__":
    main()
