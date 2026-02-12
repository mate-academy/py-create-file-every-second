from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp_now = datetime.now()
        filename = (f"app-{timestamp_now.hour}_"
                    f"{timestamp_now.minute}_"
                    f"{timestamp_now.second}") + ".log"
        timestamp_str = timestamp_now.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "w") as f:
            f.write(timestamp_str)

        print(f"{timestamp_str} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
