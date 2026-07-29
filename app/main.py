from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:

        current_time = datetime.now()
        current_hours = current_time.hour
        current_minutes = current_time.minute
        current_seconds = current_time.second

        with open(
            f"app-{current_hours}_{current_minutes}_{current_seconds}.log", "w"
        ) as new_file:

            new_file.write(str(current_time))

        print(
            str(current_time),
            f"app-{current_hours}_{current_minutes}_{current_seconds}.log"
        )

        sleep(1)


if __name__ == "__main__":
    main()
