import time

from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        time_now = datetime.now()
        hours = time_now.hour
        minutes = time_now.minute
        seconds = time_now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as f:

            f.write(time_now.strftime("%Y-%m-%d %H:%M:%S"))
            print(time_now.strftime("%Y-%m-%d %H:%M:%S")
                  + f" {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
