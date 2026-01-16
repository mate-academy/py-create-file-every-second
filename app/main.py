import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = (f"app-{current_time.hour}_"
                    f"{current_time.minute}_"
                    f"{current_time.second}.log")
        with open(filename, "w") as file:
            file.write(str(current_time))
        print(current_time, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
