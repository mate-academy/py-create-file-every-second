from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        file_name = f"app-{datetime.now().strftime('%Y%m%d-%H_%M_%S')}.log"

        with open(file_name, "w") as f:
            f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
