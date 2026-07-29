from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        with open(
                f"app-{current_date.hour}_"
                f"{current_date.minute}_"
                f"{current_date.second}.log",
                "w"
        ) as f:
            f.write(str(current_date))
        print(current_date, f.name)
        sleep(1)


if __name__ == "__main__":
    main()
