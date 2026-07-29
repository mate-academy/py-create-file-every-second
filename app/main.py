from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)

        filename = f"app-{now.hour:02}_{now.minute:02}_{now.second:02}.log"

        with open(filename, "w") as f:
            f.write(str(now))

        print(now, filename)

        time.sleep(1)


if __name__ == "__main__":
    main()
