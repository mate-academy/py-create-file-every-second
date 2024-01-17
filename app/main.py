from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        with open(file_name, "w") as f:
            f.write(str(current_time))
        print(current_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
