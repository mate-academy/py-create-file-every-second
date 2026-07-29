from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        with open(file_name, "a") as f:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(current_time)
            print(current_time + " " + file_name)
            sleep(1)


if __name__ == "__main__":
    main()
