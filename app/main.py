from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        name_file = (f"app-{time_now.hour}_{time_now.minute}_"
                     f"{time_now.second}.log")
        with open(name_file, "w") as file:
            file.write(f"{time_now}")

        print(time_now, name_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
