from datetime import datetime
from time import sleep

# DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-"
                     f"{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}"
                     f".log")
        with open(file_name, "w") as f:
            f.write(str(current_time))
        print(f"{current_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
