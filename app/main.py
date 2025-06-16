from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:
        date_time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_stamp = datetime.now().strftime("%H_%M_%S")

        with open(f"app-{time_stamp}.log", "w") as file:
            file.write(date_time_stamp)

            print(f"{date_time_stamp} app-{time_stamp}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
