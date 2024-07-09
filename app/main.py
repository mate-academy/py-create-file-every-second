from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now_time = datetime.now()
        hours, minutes, seconds = (
            now_time.hour,
            now_time.minute,
            now_time.second
        )
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        timestamp = now_time.strftime("%Y-%m-%d %H:%M:%S.%f")

        with open(file_name, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
