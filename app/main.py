import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_date = datetime.now()
        with open(
                f"app-{current_date.hour}_"
                f"{current_date.minute}_"
                f"{current_date.second}.log", "w"
        ) as new_file:
            new_file.write(str(current_date))
            print(
                str(current_date),
                f"app-{current_date.hour}_{current_date.minute}"
                f"_{current_date.second}.log"
            )
            time.sleep(1)


if __name__ == "__main__":
    main()
