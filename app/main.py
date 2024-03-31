from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_datetime = datetime.now()

        hours, minutes, seconds = (current_datetime.hour,
                                   current_datetime.minute,
                                   current_datetime.second)

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as f:
            f.write(str(current_datetime))
            print(current_datetime, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
