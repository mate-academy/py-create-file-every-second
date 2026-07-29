from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.strftime('%H_%M_%S')}.log"
        time.sleep(1)
        with open(file_name, "w") as file:
            file.write(str(current_time))
            print(current_time, file_name)


if __name__ == "__main__":
    main()
