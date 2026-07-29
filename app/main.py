from datetime import datetime
import time


def main() -> any:
    while True:
        time_now = datetime.now().strftime("%H_%M_%S")
        file_name = f"app-{time_now}.log"
        with open(file_name, "w") as file:
            file.write(f"{datetime.now()}")
            print(f"{datetime.now()} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
