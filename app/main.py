from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        hour = time_now.hour
        minute = time_now.minute
        second = time_now.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(file_name, "w") as f:
            f.write(str(datetime.now()))

        with open(file_name, "r") as f:
            print(f.read(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
