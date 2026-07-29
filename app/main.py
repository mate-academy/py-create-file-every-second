from datetime import datetime
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        current_file = (f"app-{current_time.hour}_"
                        f"{current_time.minute}_"
                        f"{current_time.second}.log")

        with open(current_file, "w") as f:
            f.write(str(current_time))
            print(f"{current_time} {current_file}")

        time.sleep(1)


if __name__ == "__main__":
    main()
