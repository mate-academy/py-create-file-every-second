import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        new_file = open(f"app-{current_time.hour}"
                        f"_{current_time.minute}"
                        f"_{current_time.second}.log", "w")
        new_file.write(str(current_time))
        print(datetime.now(), new_file.name)
        time.sleep(1)


if __name__ == "__main__":
    main()
