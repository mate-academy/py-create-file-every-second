from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_content_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file_name_timestamp = current_time.strftime("%H_%M_%S")
        file_name = f"app-{file_name_timestamp}.log"
        try:
            with open(file_name, "w") as f:
                f.write(file_content_timestamp)
            print(f"{file_content_timestamp} {file_name}")
        except Exception as e:
            print(f"Error creating file {file_name}: {e}")

        time.sleep(1)


if __name__ == "__main__":
    main()
