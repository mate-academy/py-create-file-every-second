from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = f"app-{datetime.now().hour}_" \
                   f"{datetime.now().minute}_" \
                   f"{datetime.now().second}.log"
        timestamp = f"{datetime.now().date()} " \
                    f"{datetime.now().time().hour}:" \
                    f"{datetime.now().time().minute}:" \
                    f"{datetime.now().time().second}"
        try:
            file_output = open(filename, "w")
            file_output.write(timestamp)
            sleep(1)
        except KeyboardInterrupt:
            break
        finally:
            print(f"{timestamp} {filename}")


if __name__ == "__main__":
    main()
