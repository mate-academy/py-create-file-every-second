from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        today = str(datetime.now())
        with open(
                f"app-{today[11:13]}_{today[14:16]}_{today[17:]}.log", "w"
        ) as opened_file:
            opened_file.write(today)
            print(
                f"{today} app-{today[11:13]}_{today[14:16]}_{today[17:19]}.log"
            )
        sleep(1)


if __name__ == "__main__":
    main()
