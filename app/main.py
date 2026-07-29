import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_date = datetime.now()
        current_time = current_date.time()
        file_name = (f"app-{str(current_time)[:2]}"
                     f"_{str(current_time)[3:5]}"
                     f"_{str(current_time)[6:8]}.log")

        with open(file_name, "w") as file:
            log = str(datetime.now())
            file.write(log)

        print(log, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
