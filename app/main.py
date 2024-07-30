import time
from datetime import datetime


def main() -> None:
    while True:
        timestamp = datetime.now()
        str_timestamp = str(timestamp)
        file_name = (
            f"app-{timestamp.hour}"
            f"_{timestamp.minute}"
            f"_{timestamp.second}.log"
        )

        with open(file_name, "w") as log:
            log.write(str_timestamp)

        print(f"{str_timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
