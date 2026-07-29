from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date_time = datetime.now()
        text = (f"app-{date_time.hour}_{date_time.minute}_"
                f"{date_time.second}.log")
        date_format = date_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(text, "a") as f:
            f.write(f"{date_format}")
        print(f"{date_format} {text}")
        time.sleep(1)


if __name__ == "__main__":
    main()
