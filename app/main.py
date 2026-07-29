from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        stamp = datetime.now().replace(microsecond=0)
        filename = (f"app-{stamp.hour}_{stamp.minute}_"
                    f"{stamp.second}.log")

        with open(filename, "w") as log_file:
            log_file.write(str(stamp))
            print(stamp, filename)

        sleep(1)


if __name__ == "__main__":
    main()
