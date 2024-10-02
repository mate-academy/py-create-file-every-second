from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:
        current_time = datetime.now()
        with open(f"app-{current_time.hour}_{current_time.minute}"
                  f"_{current_time.second}.log", "x") as file:
            file.write(f"{current_time}")
            print(f"{current_time} {file.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
