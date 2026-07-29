from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:

        current = datetime.now()
        current_hours = current.hour
        current_minutes = current.minute
        current_seconds = current.second

        with open(
            f"app-{current_hours}_{current_minutes}_{current_seconds}.log", "w"
        ) as new_file:

            new_file.write(str(current))

        print(
            str(current),
            f"app-{current_hours}_{current_minutes}_{current_seconds}.log"
        )

        sleep(1)


if __name__ == "__main__":
    main()
