from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        time_now = (f"app-{timestamp.hour}"
                    f"_{timestamp.minute}_{timestamp.second}.log")

        with open(time_now, "w") as f:
            f.write(str(timestamp))

        print(f"{timestamp} {time_now}")
        sleep(1)


if __name__ == "__main__":
    main()
