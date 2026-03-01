from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name =\
            f"app-{now.hour:02}_{now.minute:02}_{now.second:02}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(f"{timestamp}")
        print(timestamp, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
