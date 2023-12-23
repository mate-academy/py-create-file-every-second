from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_date_time = datetime.now()
        with open(
                f"app-{
                current_date_time.hour
                }_{
                current_date_time.minute
                }_{
                current_date_time.second
                }.log", "w"
        ) as file:
            file.write(str(current_date_time))
            print(f"{current_date_time} "
                  f"app-{current_date_time.hour}_"
                  f"{current_date_time.minute}_"
                  f"{current_date_time.second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
