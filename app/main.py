from datetime import datetime
import time   # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        cur_time = datetime.now()
        file_name = (f"app-{cur_time.hour}"
                     f"_{cur_time.minute}_"
                     f"{cur_time.second}.log")
        with open(file_name, "w") as f:
            f.write(str(cur_time))
        print(f"{cur_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
