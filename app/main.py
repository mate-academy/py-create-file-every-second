from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second

        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(
                file_name,
                "w",
                encoding="utf-8"
        ) as data_file:
            data_file.write(str(now))
            print(f"{now} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
