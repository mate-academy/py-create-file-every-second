import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> str:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(f"{file_name}", "w") as file:
            file.write(f"{now}")
        print(f"{now} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
