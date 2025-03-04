from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}" \
            f"_{now.second}.log"
        with open(file_name, "w") as f:
            f.write(str(now))
            time.sleep(1)
        print(str(now), file_name)
    pass


if __name__ == "__main__":
    main()
