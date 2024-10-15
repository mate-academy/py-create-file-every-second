from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        timestamp = str(current_time)

        try:
            with open(file_name, "w") as file:
                file.write(timestamp)
                print(f"{timestamp} {file_name}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(1)


if __name__ == "__main__":
    main()
