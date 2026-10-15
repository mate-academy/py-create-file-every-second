from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = (
            f"app-{current_time.hour}_"
            f"{current_time.minute}_{current_time.second}.log"
        )
        with open(filename, "w") as file:
            file.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        print(
            f"{current_time.strftime('%Y-%m-%d %H:%M:%S')} {filename}"
        )
        sleep(1)


if __name__ == "__main__":
    main()
