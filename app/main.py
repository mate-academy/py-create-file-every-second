from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        log_format = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(log_format, "w") as file:
            file.write(str(now))
        print(f"{now} {log_format}")
        sleep(1)


if __name__ == "__main__":
    main()
