from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        str_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{current_time.hour}_{current_time.minute}_{current_time.second}.log"
        with open(file_name, "w") as f:
            f.write(str_current_time)
            print(str_current_time, file_name)
            time.sleep(1)

if __name__ == "__main__":
    main()
