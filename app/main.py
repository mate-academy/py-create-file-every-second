from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time
import os


def main():
    try:
        while True:
            current_time = datetime.now()
            file_name = f"app-{current_time.strftime('%H_%M_%S')}.log"
            file_content = current_time.strftime('%Y-%m-%d %H:%M:%S')

            with open(file_name, "w") as f:
                f.write(file_content)
                print(f"{file_content} {file_name}")
                time.sleep(1)
    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
