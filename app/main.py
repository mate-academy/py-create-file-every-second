from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        formatted_file = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(formatted_file, "w") as f:
            f.write(time_stamp)
            print(f"{time_stamp} {formatted_file}")
        time.sleep(1)


if __name__ == "__main__":
    main()
