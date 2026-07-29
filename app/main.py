import time
from datetime import datetime


def main() -> None:
    while True:
        time_now = datetime.now()
        full_file_name = (
            f"app-{time_now.hour}"
            f"_{time_now.minute}"
            f"_{time_now.second}.log"
        )
        with open(full_file_name, "w") as file:
            file.write(str(time_now))
            print(time_now, full_file_name)
            time.sleep(1)


if __name__ == "__main__":
    main()
