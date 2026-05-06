from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(f"{file_name}", "w") as f:
            f.write(str(now))
        time.sleep(1)
        print(f"{now} {file_name}")


if __name__ == "__main__":
    main()
