import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        current_time = datetime.now()
        file_path = f"app-{current_time.strftime('%H_%M_%S')}.log"
        file_row = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "w") as file:
            file.write(file_row)
        print(f"{file_row} {file_path}")
        time.sleep(1)


if __name__ == "__main__":
    main()
