import time
from datetime import datetime


def main() -> None:

    while True:

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (
            f"app-{current_time.hour}_"
            f"{current_time.minute}_{current_time.second}.log"
        )
        with open(file_name, "w") as f:
            f.write(formatted_time)
        print(formatted_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
