from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import  sleep


def main() -> any:
    while True:
        current_time = datetime.now()

        file_name = (f"app-{current_time.hour}_{current_time.minute}"
                     f"_{current_time.second}.log")
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
