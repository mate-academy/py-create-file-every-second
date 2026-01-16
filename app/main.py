import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as f:
            f.write(f"{current_time}")

        print(current_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
