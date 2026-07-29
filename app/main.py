from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main(limit: int = None) -> None:
    count = 0
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "w") as f:
            f.write(timestamp_str)
        print(f"{timestamp_str} {filename}")
        count += 1
        if limit is not None and count >= limit:
            break
        sleep(1)


if __name__ == "__main__":
    main(limit=2)
