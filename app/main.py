from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now().strftime("%H_%M_%S")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{current_time}.log"

        with open(file_name, "w") as file:
            file.write(timestamp)
        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
