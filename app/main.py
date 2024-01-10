from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.hour}_{current_time.minute}_{current_time.second}.log"  # noqa: E501

        with open(file_name, "w") as file:
            file.write(f"{current_time.date()} {current_time.time()}")

        print(f"{current_time.date()} {current_time.time()} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
