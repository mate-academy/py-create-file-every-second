import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.hour}_" \
                    f"{current_time.minute}_{current_time.second}.log"
        with open(file_name, "w") as f:
            f.write(f"{current_time}")
        with open(file_name, "r") as f:
            print(f"{f.read()} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
