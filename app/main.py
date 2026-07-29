import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        date_now = datetime.now()

        file_name = (f"app-{date_now.hour}_"
                     f"{date_now.minute}_"
                     f"{date_now.second}.log"
                     )

        timestamp = date_now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            f.write(timestamp)

        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
