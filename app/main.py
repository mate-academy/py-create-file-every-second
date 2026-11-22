from datetime import datetime
import time


def main() -> None:
    while True:
        now_time_for_file = datetime.now().strftime("%H_%M_%S")
        with open(f"app-{now_time_for_file}.log", "a") as f:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time.sleep(1)
            f.write(f"{now}")
            file_name = f"app-{now_time_for_file}.log"
            print(f"{now} {file_name}")


if __name__ == "__main__":
    main()
