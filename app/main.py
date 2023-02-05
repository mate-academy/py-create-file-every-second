from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now().strftime("%H_%M_%S")
        file_name = f"app-{current_time}.log"
        with open(file_name, "a") as f:
            f.write(f"{datetime.now()}")
            print(f"{datetime.now()} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
