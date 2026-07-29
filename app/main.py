from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:

        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_{current_time.second}.log")

        with open(file_name, "w") as file:

            timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp_str}")

        print(f"{timestamp_str} {file_name}")

        sleep(1.0)


if __name__ == "__main__":
    main()
