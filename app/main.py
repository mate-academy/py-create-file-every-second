from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    try:
        while True:
            current_time = datetime.now()
            file_name = (f"app-{current_time.hour}_{current_time.minute}_"
                         f"{current_time.second}.log")
            timestamp = str(current_time)
            with open(file_name, "w") as file:
                file.write(timestamp)
            print(f"{timestamp} {file_name}")
            sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt("\nProgram terminated by user")


if __name__ == "__main__":
    main()
