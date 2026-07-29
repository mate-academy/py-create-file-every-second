from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_time = datetime.now().strftime("%H_%M_%S")
        time_for_file = f"app-{formatted_time}.log"

        with open(time_for_file, "w") as f:
            f.write(time_now)

        print(f"{time_now} {time_for_file}")
        sleep(1)


if __name__ == "__main__":
    main()
