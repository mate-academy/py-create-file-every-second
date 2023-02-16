import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        now = str(datetime.now())

        with open(file_name, "w") as f:
            f.write(now)
        print(f"{now} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
