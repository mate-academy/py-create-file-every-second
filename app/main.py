import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        time_stamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{current_time.hour}" \
                    f"_{current_time.minute}" \
                    f"_{current_time.second}.log"
        with open(file_name, "w") as file:
            file.write(str(current_time))
        print(f"{time_stamp} {file_name}")

        time.sleep(1)

        with open(file_name, "r") as f:
            f.read()


if __name__ == "__main__":
    main()
