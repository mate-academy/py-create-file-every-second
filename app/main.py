from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        with open(
            f"app-{now.hour}_{now.minute}_{now.second}.log",
            "w"
        ) as file_time:
            file_time.write(str(now))
        print(now, file_time.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
