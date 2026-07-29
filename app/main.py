import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        cur_time = datetime.now()
        file_name = (f"app-{cur_time.hour}_"
                     f"{cur_time.minute}_{cur_time.second}.log")
        with open(file_name, "a+") as file:
            file.write(f"{cur_time}")
            print(f"{cur_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
