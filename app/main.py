from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        c_time = datetime.now()
        with open(
                f"app-{c_time.hour}_{c_time.minute}_"
                f"{c_time.second}.log", "w"
        ) as file:
            file.write(f"{c_time}")
            print(
                c_time,
                f"app-{c_time.hour}_{c_time.minute}_"
                f"{c_time.second}.log"
            )
            time.sleep(1)


if __name__ == "__main__":
    main()
