import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        with open(f"app-{current_time.hour}"
                  f"_{current_time.minute}"
                  f"_{current_time.second}.log", "w") as f:
            f.write(f"{current_time}")
            print(f"{current_time} {f.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
