import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = str(datetime.now())
        hours = time_now[11:13]
        minutes = time_now[14:16]
        seconds = time_now[17:19]

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as file:
            file.write(f"{time_now}")

        with open(file_name) as file:
            print(f"{file.read()} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
