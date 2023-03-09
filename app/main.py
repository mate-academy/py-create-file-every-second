import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_data_time = datetime.now()
        with open(f"app-{current_data_time.hour}_"
                  f"{current_data_time.minute}_"
                  f"{current_data_time.second}.log", "w") as file:
            file.write(str(current_data_time))
        print(current_data_time, file.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
