from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        with open(f"app-{str(now.hour)}_"
                  f"{str(now.minute)}_"
                  f"{str(now.second)}.log", "w") as f:
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            file_name = (f"app-{str(now.hour)}_"
                         f"{str(now.minute)}_"
                         f"{str(now.second)}.log")
            f.write(timestamp)
            print(timestamp, file_name)
            sleep(1)


if __name__ == "__main__":
    main()
