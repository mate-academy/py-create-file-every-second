from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "a") as f:
            f.write(str(now))
        print(f"{now} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
