from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_file_name = (f"app-{datetime.now().hour}"
                             f"_{datetime.now().minute}"
                             f"_{datetime.now().second}.log")
        with open(current_file_name, "w") as file_log:
            file_log.write(f"{datetime.now()}")
        print(f"{datetime.now()} {current_file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
