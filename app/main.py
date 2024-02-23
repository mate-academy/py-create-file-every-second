from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        file_name = f"app-{hours}_{minutes}_{seconds}"
        with open(f"{file_name}.log", "a") as f:
            now_time = datetime.now()
            f.write(f"{now_time}")
        print(f"{now_time} {file_name}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
