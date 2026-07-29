from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_t = datetime.now()
        file_name = (
            f"app-{current_t.hour}_{current_t.minute}_{current_t.second}.log"
        )
        timestamp = current_t.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
