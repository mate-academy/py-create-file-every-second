from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        file_name = f"app-{datetime.now().hour}_" \
                    f"{datetime.now().minute}_" \
                    f"{datetime.now().second}.log"
        with open(f"{file_name}", "w") as file:
            file.write(f"{datetime.now()}")
            print(f"{datetime.now()} {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
