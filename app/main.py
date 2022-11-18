import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        file_name = f"app-{datetime.now().hour}_" \
                    f"{datetime.now().minute}_" \
                    f"{datetime.now().second}.log"
        current_time = datetime.now()
        with open(file_name, "w") as f:
            f.write(f"{current_time}")
            print(f"{current_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
