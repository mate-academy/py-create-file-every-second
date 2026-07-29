from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.time().hour
        minutes = now.time().minute
        seconds = now.time().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
