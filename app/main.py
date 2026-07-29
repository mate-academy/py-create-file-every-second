from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        new_file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(f"{new_file_name}", "w+") as file:
            file.write(f"{now}")
        print(f"{now} {new_file_name}")
        time.sleep(0.999)


if __name__ == "__main__":
    main()
