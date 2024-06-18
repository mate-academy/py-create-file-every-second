from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        with open(
                f"app-{current_time.hour}_"
                f"{current_time.minute}_{
                current_time.second}.log", "w") as f:
            f.write(f"{datetime.now()}")
        print(f"{current_time} {f.name}")
        sleep(1)


if __name__ == "__main__":
    main()
