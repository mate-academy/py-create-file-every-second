from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:
        time.sleep(1)
        now_time = datetime.now()
        timestamp = now_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now_time.strftime('%H_%M_%S')}.log"
        with open(file_name, "a") as file:
            file.write(f"{timestamp}\n")
        print(timestamp, file_name)


if __name__ == "__main__":
    main()
