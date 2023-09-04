from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_date = datetime.now()
        file_name = (
            f"app-{current_date.hour}"
            f"_{current_date.minute}"
            f"_{current_date.second}.log"
        )

        with open(file_name, "w") as f:
            f.write(str(current_date))
            time.sleep(1)
        print(f"{current_date} {file_name}")


if __name__ == "__main__":
    main()
