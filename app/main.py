from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_and_time = datetime.now()
        with open(
                f"app-{date_and_time.hour}_{date_and_time.minute}_"
                + f"{date_and_time.second}.log",
                "w"
        ) as file:
            file.write(str(date_and_time))
            print(date_and_time, file.name)

        sleep(1)


if __name__ == "__main__":
    main()
