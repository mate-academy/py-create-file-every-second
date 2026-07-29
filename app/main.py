import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        file_time = (
            f"app-{current_time.hour}"
            f"_{current_time.minute}"
            f"_{current_time.second}.log"
        )
        with open(file_time, "w") as tim:
            tim.write(str(current_time))
            print(f"{datetime.now()} {file_time}")
            time.sleep(1)


if __name__ == "__main__":
    main()
