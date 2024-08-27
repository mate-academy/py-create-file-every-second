from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        filename = (f"app-{datetime.now().hour}_"
                    f"{datetime.now().minute}_"
                    f"{datetime.now().second}.log")
        new_file = open(filename, "w")
        current_time_str = str(datetime.now())
        new_file.write(current_time_str)
        print(f"{current_time_str} {filename}")
        new_file.close()
        sleep(1)


if __name__ == "__main__":
    main()
