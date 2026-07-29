from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:

        now_time = datetime.now()
        timestamp = now_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now_time.strftime('%H_%M_%S')}.log"
        with open(file_name, "a") as file:
            file.write(f"{timestamp}")
        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
