import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date_and_time = datetime.now()
        name_file = f"app-{date_and_time.hour}_" \
                    f"{date_and_time.minute}_" \
                    f"{date_and_time.second}"
        with open(f"{name_file}.log", "w") as file:
            file.write(str(date_and_time))
            print(date_and_time, f"{name_file}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
