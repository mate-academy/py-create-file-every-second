from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (
            f"app-{current_time.hour}_{current_time.minute}"
            f"_{current_time.second}.log"
        )
        timestamp = str(current_time).split(".")[0]
        new_file = open(file_name, "w")
        new_file.write(timestamp)
        new_file.close()
        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
