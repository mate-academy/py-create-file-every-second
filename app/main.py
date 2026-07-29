from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()

        hours = now.hour
        minutes = now.minute
        seconds = now.second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as f:
            f.write(str(now))

        print(str(now), file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
