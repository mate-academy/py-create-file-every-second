from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time = datetime.now()

        with open(f"app-{date_time.hour}_{date_time.minute}"
                  f"_{date_time.second}.log", "w") as file_:
            file_.write(f"{date_time}")
            print(f"{date_time} {file_.name}")
        sleep(1)


if __name__ == "__main__":
    main()
