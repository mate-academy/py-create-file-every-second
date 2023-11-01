from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as fh:
            fh.write(f"{time_stamp}")
        print(f"{time_stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
