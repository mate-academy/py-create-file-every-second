import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> str:
    try:
        while True:
            time_now = datetime.now()
            filename = (
                f"app-{time_now.hour}_{time_now.minute}_"
                f"{time_now.second}.log"
            )
            timestamp = (
                f"{time_now.year}-{time_now.month}-{time_now.day} "
                f"{time_now.hour}:{time_now.minute}:{time_now.second}"
            )
            with open(filename, "w") as file:
                file.write(timestamp)
            print(f"{timestamp} {filename}")
            time.sleep(1)

    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
