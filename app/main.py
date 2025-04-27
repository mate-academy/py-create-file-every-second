from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time
import os


def main() -> None:
    while True:
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.strftime("%H_%M_%S")}.log"
        file_path = os.path.join(os.getcwd(), file_name)

        try:
            with open(file_path, "w") as log_file:
                log_file.write(time_stamp)
            print(f"{time_stamp} {file_name}")
        except Exception as e:
            print(f"Error creating file: {e}")
        time.sleep(1)


if __name__ == "__main__":
    main()
