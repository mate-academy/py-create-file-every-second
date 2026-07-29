from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:
            data_to_write = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(data_to_write)
        print(f"{data_to_write} app-{hours}_{minutes}_{seconds}.log")
        sleep(1)


if __name__ == "__main__":
    main()
