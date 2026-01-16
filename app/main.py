from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        timestamp = " ".join(now.isoformat().split("T"))
        with open(file_name, "w") as f:
            f.write(timestamp)
        print(timestamp, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
