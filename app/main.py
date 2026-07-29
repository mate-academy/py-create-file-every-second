from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    try:
        while True:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            filename = now.strftime("app-%H_%M_%S.log")
            with open(filename, "w") as f:
                f.write(timestamp)
            print(timestamp, filename, flush=True)
            sleep(1)
    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
