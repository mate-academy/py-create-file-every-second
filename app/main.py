import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while 1:
        start = datetime.now()
        start_str = start.strftime("%Y-%m-%d %H:%M:%S")

        filename = f"app-{start.hour}_{start.minute}_{start.second}.log"

        with open(filename, "w") as f:
            f.write(start_str)
        time.sleep(1)
        print(f"{start_str} {filename}")


if __name__ == "__main__":
    main()
