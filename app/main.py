from time import sleep
from datetime import datetime


def create_and_print_file() -> None:
    current_time = datetime.now()
    filename = (f"app-{current_time.hour:02d}_{current_time.minute:02d}"
                f"_{current_time.second:02d}.log")
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as f:
        f.write(timestamp)

    print(f"{timestamp} {filename}")


def main() -> None:
    while True:
        create_and_print_file()
        sleep(1)


if __name__ == "__main__":
    main()
