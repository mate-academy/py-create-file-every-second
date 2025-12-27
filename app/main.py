from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    try:
        while True:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            name_file = f"app-{now.hour}_{now.minute:02d}_{now.second:02d}.log"
            with open(name_file, "a") as log:
                log.write(timestamp)
                print(timestamp, name_file)
            sleep(1)
    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
