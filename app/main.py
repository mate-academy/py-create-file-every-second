from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        cur_time = datetime.now()
        file_name = \
            f"app-{cur_time.hour}_{cur_time.minute}_{cur_time.second}.log"

        with open(file_name, "w") as file:
            file.write(f"{cur_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{cur_time.strftime('%Y-%m-%d %H:%M:%S')} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
