from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now_time = datetime.now()
        file_name = \
            (f"app-{now_time.hour}_{now_time.minute}_{now_time.second}.log")
        times = now_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(times)
        print(f"{times} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
