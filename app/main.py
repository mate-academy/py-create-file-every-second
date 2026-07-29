from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        filename = (f"app-{time_now.hour}_"
                    f"{time_now.minute}_"
                    f"{time_now.second}.log")
        with open(filename, "w") as new_file:
            new_file.write(time_now.strftime("%Y-%m-%d %H:%M:%S"))
        print(time_now, end=" ")
        print(filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
