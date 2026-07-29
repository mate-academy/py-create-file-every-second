import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT

CONTENT_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
FILENAME_TIME_FORMAT = "%H_%M_%S"
FILENAME_PREFIX = "app"
FILENAME_EXT = "log"


def main() -> None:

    while True:
        now = datetime.now()
        content_timestamp = now.strftime(CONTENT_TIMESTAMP_FORMAT)
        time_part = now.strftime(FILENAME_TIME_FORMAT)
        file_name = f"{FILENAME_PREFIX}-{time_part}.{FILENAME_EXT}"
        with open(file_name, "w") as f:
            f.write(content_timestamp)
        print(f"{content_timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
