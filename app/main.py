from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_{current_time.minute}_"
                     f"{current_time.second}.log")
        with open(file_name, "w+") as f:
            f.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
            f.seek(0)
            print(f.read() + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
