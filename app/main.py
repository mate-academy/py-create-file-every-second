from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> any:

    while True:
        dt = datetime.now()
        file_name = f"app-{dt.hour}_{dt.minute}_{dt.second}.log"
        timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name,
                  mode="w",
                  encoding="utf-8",
                  newline="") as f:
            f.write(timestamp)
            print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
