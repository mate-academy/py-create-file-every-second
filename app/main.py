import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (
            f"app-{current_time.hour}"
            f"_{current_time.minute}_"
            f"{current_time.second}.log"
        )

        with open(file_name, "w") as file:
            file.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))

        print(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
