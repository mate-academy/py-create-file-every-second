from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = (f"app-"
                     f"{now.hour:02d}_"
                     f"{now.minute:02d}_"
                     f"{now.second:02d}.log"
                     )
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            f.write(timestamp)
            print(timestamp, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
