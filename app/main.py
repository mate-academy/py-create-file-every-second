from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()

        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w") as file:
            file.write(f"{timestamp_str}")

        print(f"{timestamp_str} {file_name}")

        sleep(1)
        file.close()


if __name__ == "__main__":
    main()
