import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:

        now_time = datetime.now()

        hour = now_time.hour
        minute = now_time.minute
        second = now_time.second

        filename = f"app-{hour}_{minute}_{second}.log"

        with open(filename, "w") as file:
            file.write(now_time.strftime("%Y-%m-%d %H:%M:%S"))

        print(f"{now_time.strftime('%Y-%m-%d %H:%M:%S')} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
