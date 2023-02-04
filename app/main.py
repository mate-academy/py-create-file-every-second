import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        value = datetime.now()
        with open(
                f"app-{value.hour}_{value.minute}_{value.second}.log", "w"
        ) as f:
            f.write(f"{value}")
            print(value, f"app-{value.hour}_{value.minute}_{value.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
