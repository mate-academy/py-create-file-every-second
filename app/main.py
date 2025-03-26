from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        with open(
                f"app-{current_time.hour}_{current_time.minute}_"
                f"{current_time.second}.log", "w"
        ) as file:
            file.write(f"{current_time}")
        print(
            current_time,
            f"app-{current_time.hour}_{current_time.minute}_"
            f"{current_time.second}.log"
        )
        time.sleep(1)


if __name__ == "__main__":
    main()
