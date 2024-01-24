import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        times = now.time()

        hours, minutes, seconds = str(times).split(":")

        file_name = f"app-{hours}_{minutes}_{seconds[:2]}.log"

        with open(file_name, "a") as file:
            file.write(f"{str(now)}")

        print(f"{datetime.now()} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
