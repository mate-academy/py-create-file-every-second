from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time
from typing import Any


def main() -> Any:
    while True:
        current_time = datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        filename_str = current_time.strftime("app-%H_%M_%S.log")
        with open(filename_str, "w") as f:
            f.write(timestamp_str)
        print(f"{timestamp_str} {filename_str}")
        time.sleep(1)


if __name__ == "__main__":
    main()
