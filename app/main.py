from __future__ import annotations

from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (
            f"app-{timestamp.hour}_"
            f"{timestamp.minute}_{timestamp.second}.log"
        )

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(formatted_timestamp)

        print(f"{formatted_timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
