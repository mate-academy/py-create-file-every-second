import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = (f"app-{time_now.hour}_"
                     f"{time_now.minute}_"
                     f"{time_now.second}.log")
        with open(file_name, "w") as f:
            f.write(str(time_now))

        print(f"{time_now} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
