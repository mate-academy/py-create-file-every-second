from datetime import datetime  # DO NOT CHANGE THIS IMPORT

import time


def main() -> None:

    while True:
        today = datetime.now()
        hours = str(today.hour)
        minutes = str(today.minute)
        seconds = str(today.second)
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(today))
            print(f"{today} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
