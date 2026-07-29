import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        present = datetime.now()
        times = present.time()
        hours, minutes, seconds = str(times).split(":")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "a") as file:
            file.write(f"{str(present)}")

        print(datetime.now(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
