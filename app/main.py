import time
from datetime import datetime


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = f"app-{current_time.hour}_{current_time.minute}"\
                   f"_{current_time.second}.log"
        with open(filename, "w") as f:
            f.write(f"{current_time}")
            print(f"{current_time} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
