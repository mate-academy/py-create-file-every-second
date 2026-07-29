from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:

        now = datetime.now()
        current_hours = now.hour
        current_minutes = now.minute
        current_seconds = now.second

        with open(
                f"app-{current_hours}_{current_minutes}_{current_seconds}.log",
                "w"
        ) as new_file:
            new_file.write(str(now))

        print(
            str(now),
            f"app-{current_hours}_{current_minutes}_{current_seconds}.log"
        )
        sleep(1)


if __name__ == "__main__":
    main()
