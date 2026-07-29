import time
from datetime import datetime


def main() -> None:
    while True:
        start_time = datetime.now()
        name = (f"app-{start_time.hour}_"
                f"{start_time.minute}_{start_time.second}.log")
        with open(name, "w") as f:
            f.write(f"{start_time}")
            print(start_time, name)
            time.sleep(1)


if __name__ == "__main__":
    main()
