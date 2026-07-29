from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        hour = time_now.hour
        minute = time_now.minute
        seconds = time_now.second

        file_name = f"app-{hour}_{minute}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(f"{time_now}")

        print(f"{time_now} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
