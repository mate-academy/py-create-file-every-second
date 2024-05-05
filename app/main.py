from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time
from typing import Any


def main() -> Any:
    while True:
        current_time = datetime.now()
        time.sleep(1)
        with open(f"app-{current_time.hour}_{current_time.minute}_\
{current_time.second}.log", "w") as f:
            f.write(f"{current_time}")


if __name__ == "__main__":
    main()
