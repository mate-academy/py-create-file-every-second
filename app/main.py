from datetime import datetime
import time


def main() -> None:
    while True:
        now_time = datetime.now()
        file_name = (
            f"app-{now_time.hour}_{now_time.minute}_{now_time.second}.log"
        )
        with open(file_name, "a+") as file:
            file.write(str(now_time))
            print(now_time, file_name)
            time.sleep(1)


if __name__ == "__main__":
    main()
