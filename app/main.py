import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_data = datetime.now()
        file_name = (
            f"app-{current_data.hour}"
            f"_{current_data.minute}"
            f"_{current_data.second}.log"
        )

        with open(file_name, "w") as log_file:
            log_file.write(str(current_data))
            time.sleep(1)
        print(f"{current_data} {file_name}")


if __name__ == "__main__":
    main()
