from datetime import datetime
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{current_time.strftime('%H_%M_%S')}.log"

        with open(file_name, "a") as f:
            f.write(timestamp_str)

        print(f"{timestamp_str} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
