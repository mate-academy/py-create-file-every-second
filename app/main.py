from datetime import datetime, time  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hour, minute, second = now.hour, now.minute, now.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        now_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(now_time)
        print(now_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
