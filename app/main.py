from datetime import datetime
import time


def main():
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_{current_time.second}.log")
        open(file_name, "w").write(str(current_time))
        print(current_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
