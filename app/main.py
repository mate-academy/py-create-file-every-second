from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_date = datetime.now()
        current_time = current_date.time()

        file_name_start = f"app-{current_time.hour}_{current_time.minute}"
        file_name_end = f"_{current_time.second}.log"
        file_name = f"{file_name_start}{file_name_end}"
        file_content = str(current_date)

        with open(file_name, "w") as f:
            f.write(file_content)
        print(f"{file_content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
