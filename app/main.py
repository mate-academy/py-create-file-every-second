from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        current_file = (f"app"
                        f"-{current_date.hour}"
                        f"_{current_date.minute}"
                        f"_{current_date.second}.log"
                        )

        with open(current_file, "w") as time_file:
            time_file.write(f"{current_date}")
            print(current_date, current_file)
        sleep(1)
    pass


if __name__ == "__main__":
    main()
