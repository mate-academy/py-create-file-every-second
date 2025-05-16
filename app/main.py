from datetime import datetime
import time


def main() -> None:
    while True:
        datetime_now = datetime.now().replace(microsecond=0)
        file_name = (
            f"app-{datetime_now.hour}_"
            f"{datetime_now.minute}_"
            f"{datetime_now.second}.log"
        )
        with open(file_name, "w") as f:
            f.write(str(datetime_now))
        print(datetime_now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
