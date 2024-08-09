from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        time_info = now.strftime("%Y-%m-%d %H:%M:%S")

        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w") as log:
            log.write(time_info)

        print(f"{time_info} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
