from datetime import datetime
import time


def main() -> None:
    while True:
        current_date = datetime.now()
        with open(
                f"app-{current_date.hour}_{current_date.minute}"
                f"_{current_date.second}.log", "w"
        ) as file:
            file.write(f"{datetime.now()}")

        print(
            current_date,
            f"app-{current_date.hour}_{current_date.minute}"
            f"_{current_date.second}.log"
        )
        time.sleep(1)


if __name__ == "__main__":
    main()
