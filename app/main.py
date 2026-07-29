from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        raw_timestamp = datetime.now()
        timestamp = str(raw_timestamp).split(".")[0]
        file_name = (
            f"app-{raw_timestamp.hour}_"
            f"{raw_timestamp.minute}_"
            f"{raw_timestamp.second}.log"
        )
        with open(file_name, "w") as f:
            f.write(f"{timestamp}")
        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
