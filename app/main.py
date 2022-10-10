from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        hours = time_now.time().hour
        minutes = time_now.time().minute
        seconds = time_now.time().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(time_now))
        print(f"{str(time_now)} {str(file_name)}")
        time.sleep(1)


if __name__ == "__main__":
    main()
