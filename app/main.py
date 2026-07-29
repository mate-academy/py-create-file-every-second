from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as f:
            f.write(f"{now}")

        print(f"{now} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
