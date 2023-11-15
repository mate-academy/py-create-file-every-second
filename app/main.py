from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_time = (
            f"app-{current_time.hour}_"
            f"{current_time.minute}_"
            f"{current_time.second}.log"
        )

        with open(file_time, "w") as file:
            file.write(str(current_time))

            print(f"{datetime.now()} {file_time}")
            time.sleep(1)


if __name__ == "__main__":
    main()
