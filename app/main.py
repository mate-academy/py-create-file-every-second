import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> any:
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.strftime('%H_%M_%S')}.log"
        print(current_time, file_name)
        with open(f"{file_name}", "w") as f:
            f.write(str(current_time))
        time.sleep(1)


if __name__ == "__main__":
    main()
