from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        name = (
            f"app-{current_time.hour}_"
            f"{current_time.minute}_"
            f"{current_time.second}.log"
        )
        new_file = open(name, "w")
        time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(time)
        new_file.close()
        print(time, name)
        sleep(1)
    pass


if __name__ == "__main__":
    main()
