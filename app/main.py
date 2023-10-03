import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date_time = datetime.now()
        file_name = (f"app-{date_time.hour}"
                     f"_{date_time.minute}"
                     f"_{date_time.second}.log")
        with open(file_name, "w") as file:
            file.write(str(date_time))
        print(f"{date_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
