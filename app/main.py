from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        with open(file_name, "w") as f:
            correct_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(correct_time)
            print(correct_time, file_name, flush=True)
        time.sleep(1)


if __name__ == "__main__":
    main()
