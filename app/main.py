import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = (
            f"app-"
            f"{current_time.hour}_"
            f"{current_time.minute}_"
            f"{current_time.second}.log"
        )
        with open(filename, "w") as f:
            print(current_time, filename)
            f.write(str(current_time))
            time.sleep(1)


if __name__ == "__main__":
    main()
