from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        hour = datetime.now().hour
        minute = datetime.now().minute
        second = datetime.now().second
        file_name = f"app-{hour}_{minute}_{second}.log"

        with open(file_name, "w") as file:
            time_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(time_log)
            print(f"{time_log} {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
