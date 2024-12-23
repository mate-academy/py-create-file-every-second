from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (f"app-{time_now.hour}_{time_now.minute}"
                     f"_{time_now.second}.log")
        with open(file_name, "w") as f:
            f.write(time_now.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"{time_now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
