from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    try:
        while True:
            current_time: datetime = datetime.now()
            hours: int = current_time.hour
            minutes: int = current_time.minute
            seconds: int = current_time.second
            filename: str = f"app-{hours}_{minutes}_{seconds}.log"
            timestamp_str: str = current_time.strftime("%Y-%m-%d %H:%M:%S")

            with open(filename, "w") as file:
                file.write(timestamp_str)

            print(f"{timestamp_str} {filename}")
            time.sleep(1)
    except KeyboardInterrupt:
        raise
