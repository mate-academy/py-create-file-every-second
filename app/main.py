from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        with open(
                f"app-{now.hour}_{now.minute}_{now.second}.log", "w"
        ) as new_file:
            new_file.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(
                f"{now.strftime('%Y-%m-%d %H:%M:%S')} "
                f"app-{now.hour}_{now.minute}_{now.second}.log"
            )
        time.sleep(1)


if __name__ == "__main__":
    main()
