from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_data = datetime.now()
        file_name = f"app-{current_data.hour}_{current_data.minute}_{current_data.second}.log"
        timestamp = current_data.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
