from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        filename = (f"app"
                    f"-{current_time.hour}"
                    f"_{current_time.minute}"
                    f"_{current_time.second}.log")

        with open(filename, "w") as file:
            file.write(timestamp)

        print(f"{timestamp} {filename}")

        sleep(1)


if __name__ == "__main__":
    main()
