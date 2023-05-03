from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now()
        new_file = (
            open(f"app-{time_now.hour}_"
                 f"{time_now.minute}_"
                 f"{time_now.second}.log", "w")
        )
        new_file.write(f"{time_now}")
        new_file.close()
        new_file = (
            open(f"app-{time_now.hour}_"
                 f"{time_now.minute}_"
                 f"{time_now.second}.log")
        )
        print(new_file.read(), new_file.name)
        sleep(1)


if __name__ == "__main__":
    main()
