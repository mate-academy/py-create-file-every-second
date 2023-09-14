import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = f"app" \
                    f"-{current_time.hour}" \
                    f"_{current_time.minute}" \
                    f"_{current_time.second}.log"
        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(str(current_time))
        print(f"{timestamp_str} {file_name}")

        time.sleep(1)

        with open(file_name, "r") as f:
            f.read()


if __name__ == "__main__":
    main()
