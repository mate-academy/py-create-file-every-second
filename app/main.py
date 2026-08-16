from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        with open(
                f"app-{time.hour}_{time.minute}_{time.second}.log", "w"
        ) as file:
            time_to_write = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(time_to_write)
        print(time_to_write, file.name)
        sleep(1)


if __name__ == "__main__":
    main()
