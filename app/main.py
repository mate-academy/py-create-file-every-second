from datetime import datetime
import time


def main() -> None:
    while True:
        current_date = datetime.now()
        file = (f"app-{current_date.hour}_{current_date.minute}_"
                f"{current_date.second}.log")
        with open(file, "a") as f:
            f.write(str(current_date))
            print(f"{current_date} {file}")
            time.sleep(1)


if __name__ == "__main__":
    main()
