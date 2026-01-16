from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now_time = datetime.now()
        timestamp = now_time.strftime("%Y-%m-%d %H:%M:%S")
        name_file = (f"app-{now_time.hour}_{now_time.minute}"
                     f"_{now_time.second}.log")

        with open(name_file, "w", encoding="utf-8") as output:
            output.write(timestamp)

        print(f"{timestamp} {name_file}")
        time.sleep(1)


if __name__ == "__main__":
    main()
