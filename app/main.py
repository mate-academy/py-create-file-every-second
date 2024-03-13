from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        name_file = (f"app-{current_time.hour}_{current_time.minute}_"
                     f"{current_time.second}.log")
        with open(name_file, "w") as f:
            f.write(str(current_time))
            print(current_time, name_file)
        sleep(1)


if __name__ == "__main__":
    main()
