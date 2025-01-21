from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = f"app-{time_now.strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as f:
            f.write(f"{time_now}")
        print(f"{time_now} {file_name}")
        f.close()
        time.sleep(1)


if __name__ == "__main__":
    main()
